r"""DMARC aggregate report parser"""
from xml.dom import minidom
from datetime import datetime
from StringIO import StringIO
from email.parser import Parser
import zipfile
import util

class ReportMetaData(object):
	r"""ReportMetaData - Abstract for aggregate report metadata nodes
		requires report XML as a string
		@org_name - reporting organization
		@email - organization email
		@extra_contact_info - organization contact info
		@report_id - report id
		@error - report errors, if any
		@begin - minimum date, unmodified, i.e. seconds since epoch
		@end - maximum date, unmodified, i.e. seconds since epoch
		@begin_utc_iso - min. date, utc in ISO format
		@end_utc_iso - max. date, utc in ISO format
		@begin_loc_iso - min. date, local time in ISO format
		@end_loc_iso - max. date, local time in ISO format
	"""
	def __init__(self, report):
		self.dom = minidom.parseString(report)
		self.org_name = get_text(self.dom, "org_name")
		self.email = get_text(self.dom, "email")
		self.extra_contact_info = get_text(self.dom, "extra_contact_info")
		self.report_id = get_text(self.dom, "report_id")
		self.error = get_text(self.dom, "error")
		self.begin = get_text(self.dom, "begin")
		self.end = get_text(self.dom, "end")
		self.begin_utc_iso = datetime.utcfromtimestamp(
			float(self.begin)).isoformat()
		self.end_utc_iso = datetime.utcfromtimestamp(
			float(self.end)).isoformat() 
		self.begin_loc_iso = datetime.fromtimestamp(
			float(self.begin)).isoformat()
		self.end_loc_iso = datetime.fromtimestamp(
			float(self.end)).isoformat() 

class PolicyPublished(object):
	r"""PolicyPublished - Abstract representing the published policy for 
		the reported domain.
		requires report xml as a string
		@domain - the reported domain
		@adkim - dkim alignment mode
		@aspf - spf alignment mode
		@p - policy
		@pct - percentage applied to policy
		@rf - forensic reporting format
		@ri - aggregate reporting interval
		@rua - reporting URI(s) for aggregate data
		@ruf - reporting URI(s) for forensic data
		@sp - requested sub-domain policy
		@v - specification version
		@policy - alias for 'p'
	"""
	def __init__(self, report):
		self.dom = minidom.parseString(report)
		self.domain = get_text(self.dom, "domain")
		self.adkim = get_text(self.dom, "adkim")
		self.aspf = get_text(self.dom, "aspf")
		self.p = get_text(self.dom, "p")
		self.pct = get_text(self.dom, "pct")
		self.rf = get_text(self.dom, "rf")
		self.ri = get_text(self.dom, "ri")
		self.rua = get_text(self.dom, "rua")
		self.ruf = get_text(self.dom, "ruf")
		self.sp = get_text(self.dom, "sp")
		self.v = get_text(self.dom, "v")
		self.policy = self.p

class Record(object):
	r"""Record - Abstract representing record level data
		requires record level node
		@source_ip - source ip of the messages
		@count - messages received from the ip
		@disposition - the evaluated disposition of the message
		@dkim - dkim, enumerated, pass / fail
		@spf - spf, enumerated, pass / fail
		@header_from - From: header value
		@dkim - list of dkim results
		@spf - list of spf results
		@reason - list of failure reasons
	"""
	def __init__(self, node):
		self.source_ip = get_text(node, "source_ip")
		self.count = int(get_text(node, "count"))
		self.disposition = get_text(node, "disposition")
		self.header_from = get_text(node, "header_from")
		self.dkim_nodes = node.getElementsByTagName("dkim")
		self.dkim = []
		for n in self.dkim_nodes:
			self.dkim.append({"domain": get_text(n, "domain"),
				"result": get_text(n, "result"),
				"human_result": get_text(n, "human_result")})
		self.spf_nodes = node.getElementsByTagName("spf")
		self.spf = []
		for n in self.spf_nodes:
			self.spf.append({"domain": get_text(n, "domain"),
				"result": get_text(n, "result")})
		self.reason_nodes = node.getElementsByTagName("reason")
		self.reason = []
		for n in self.reason_nodes:
			self.reason.append({"type": get_text(n, "type"),
				"comment": get_text(n, "comment")})

class Report(object):
	r"""Report - Convenience class the includes all the reporting
		abstracts
		requires a report file as a string
		@report_meta_data - ReportMetaData
		@policy_published - PolicyPublished
		@records - list of Records
	"""
	def __init__(self, report_xml):
		self.report_source = report_xml 
		self.report_meta_data = ReportMetaData(self.report_source)
		self.policy_published = PolicyPublished(self.report_source)
		self.records = [Record(r) for r in get_records(self.report_source)]

def get_records(report):
	r"""Returns a list of all record objects in a source file
		requires report as a string
	"""
	dom = minidom.parseString(report)
	records = dom.getElementsByTagName("record")
	return records

def get_text(s, t):
	r"""Returns the text for a given node"""
	try:
		return s.getElementsByTagName(t)[0].childNodes[0].data
	except IndexError:
		return None

def _unpack_from_zip(source):
	r"""Returns report XML as string
		requires zip file source
	"""
	try:
		zip_file = zipfile.ZipFile(StringIO(source), "r")
		file_name = zip_file.namelist()[0]
		return zip_file.open(file_name, "r").read()
	except Exception, e:
		return None

def report_from_email(email_source):
	r"""Returns report.Report
		requires aggregate email message as a string
	"""
	try:
		dmarc_rfc_email = Parser().parsestr(email_source)
		if dmarc_rfc_email.is_multipart():
			for part in dmarc_rfc_email.walk():
				if part.get_content_type() == "application/zip":
					source_payload = dmarc_rfc_email.get_payload(decode=1)
				else:
					pass
		else:
			source_payload = dmarc_rfc_email.get_payload(decode=1) 
		return Report(_unpack_from_zip(source_payload)) 
	except Exception, e:
		return None

def report_from_file(file_source, zipped=False):
	r"""Returns report.Report
		requires zipped arrgregate report as file path
		option zipped, default false - True if file is zipped
		report_from_file("path_to_dmarc_report")
	"""
	if z:
		return Report(_unpack_from_zip(open(file_source, "r").read())) 
	else:
		return Report(open(file_source, "r").read())
