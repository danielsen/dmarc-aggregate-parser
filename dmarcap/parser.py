"""
dmarcap/parser.py - Primary DMARC XML aggragate report parsing class
"""
from builtins import next
from builtins import object
try:
    import defusedxml.etree.cElementTree as etree
except ImportError:
    import xml.etree.cElementTree as etree

from .meta_data import MetaData
from .record import Record
from .identifiers import Identifiers
from .auth_results import AuthResults, DkimAuthentication, SpfAuthentication
from .report import Report
from .policy_evaluated import PolicyEvaluated, Reason
from .policy_published import PolicyPublished

class Parser(object):
    """Aggregate report parser base class"""
    def __init__(self, dmarc_report_xml_file):
        self.report_file = dmarc_report_xml_file

    def _get_file_iterator(self):
        return iter(etree.iterparse(self.report_file, events=("start", "end")))

    def parse_report(self):
        """Parse report into :class:`~dmarcap.report.Report`"""
        dmarc_report = Report()
        dmarc_report.meta_data = self.parse_meta_data()
        dmarc_report.policy_published = self.parse_policy_published()
        dmarc_report.records = self.parse_report_records()

        return dmarc_report

    def parse_meta_data(self):
        """Parse report meta data into :class:`~dmarcap.meta_data.MetaData`"""
        report_meta_data = MetaData()
        meta_finished = False

        context = self._get_file_iterator()
        event, root = next(context)
        for event, element in context:
            if event == "end" and element.tag == "report_metadata":
                report_meta_data.org_name = (element.findtext("org_name"))
                report_meta_data.email = (element.findtext("email"))
                report_meta_data.extra_contact_info = (element.findtext("extra_contact_info"))
                report_meta_data.report_id = (element.findtext("report_id"))
                report_meta_data.date_range_begin = (element.findtext("date_range/begin"))
                report_meta_data.date_range_end = (element.findtext("date_range/end"))

                meta_finished = True
                root.clear()
                continue

        if meta_finished:
            return report_meta_data

        return None

    def parse_policy_published(self):
        """
        Parse report published policy into
        :class:`~dmarcap.policy_published.PolicyPublished`
        """
        report_policy_published = PolicyPublished()
        report_finished = False

        context = self._get_file_iterator()
        event, root = next(context)
        for event, element in context:
            if event == "end" and element.tag == "policy_published":
                report_policy_published.domain = (element.findtext("domain"))
                report_policy_published.adkim = (element.findtext("adkim"))
                report_policy_published.aspf = (element.findtext("aspf"))
                report_policy_published.fo = (element.findtext("fo"))
                report_policy_published.p = (element.findtext("p"))
                report_policy_published.pct = (element.findtext("pct"))
                report_policy_published.rf = (element.findtext("rf"))
                report_policy_published.ri = (element.findtext("ri"))
                report_policy_published.rua = (element.findtext("rua"))
                report_policy_published.sp = (element.findtext("sp"))
                report_policy_published.v = (element.findtext("v"))

                report_finished = True
                root.clear()
                continue

        if report_finished:
            return report_policy_published

        return None

    def parse_report_records(self):
        """
        Parse aggregate report records into a list of
        :class:`~dmarcap.record.Record`
        """
        records = []

        context = self._get_file_iterator()
        event, root = next(context)
        for event, element in context:
            if event == "end" and element.tag == "record":
                report_record = Record()
                report_record.identifiers = Identifiers()
                report_record.policy_evaluated = PolicyEvaluated()

                report_record.auth_results = AuthResults()
                report_record.auth_results.dkim = DkimAuthentication()
                report_record.auth_results.spf = SpfAuthentication()

                report_record.count = (element.findtext("row/count"))
                report_record.source_ip = (element.findtext("row/source_ip"))

                report_record.identifiers.header_from = (
                    element.findtext("identifiers/header_from"))
                report_record.identifiers.envelope_to = (
                    element.findtext("identifiers/envelope_to"))
                report_record.identifiers.envelope_from = (
                    element.findtext("identifiers/envelope_from"))

                report_record.policy_evaluated.disposition = (
                    element.findtext("row/policy_evaluated/disposition"))
                report_record.policy_evaluated.dkim = (
                    element.findtext("row/policy_evaluated/dkim"))
                report_record.policy_evaluated.spf = (
                    element.findtext("row/policy_evaluated/spf"))
                report_record.policy_evaluated.reasons = [
                    Reason(reason.find('type').text, reason.find('comment').text)
                    for reason in element.findall('row/policy_evaluated/reason')
                ]

                report_record.auth_results.dkim.domain = (
                    element.findtext("auth_results/dkim/domain"))
                report_record.auth_results.dkim.selector = (
                    element.findtext("auth_results/dkim/selector"))
                report_record.auth_results.dkim.result = (
                    element.findtext("auth_results/dkim/result"))
                report_record.auth_results.dkim.human_result = (
                    element.findtext("auth_results/dkim/human_result"))

                report_record.auth_results.spf.domain = (
                    element.findtext("auth_results/spf/domain"))
                report_record.auth_results.spf.result = (
                    element.findtext("auth_results/spf/result"))
                report_record.auth_results.spf.scope = (
                    element.findtext("auth_results/spf/scope"))

                records.append(report_record)
                root.clear()
                continue

        return records
