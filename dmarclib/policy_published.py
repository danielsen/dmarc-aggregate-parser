"""
dmarclib/policy_published.py - Representation of the policy_published of a
DMARC XML aggregate report. For more information, refer to
https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class PolicyPublished(object):
    """Representation of policy_published"""
    def __init__(self):
        self.domain = None
        self.adkim = None
        self.aspf = None
        self.fo = None
        self.p = None
        self.pct = None
        self.rf = None
        self.ri = None
        self.rua = None
        self.ruf = None
        self.sp = None
        self.v = None
        self.failure_reporting_options = self.fo
        self.policy = self.p
        self.percent = self.pct
        self.report_format = self.rf
        self.report_interval = self.ri
        self.report_uri_aggregate = self.rua
        self.report_uri_forensic = self.ruf
        self.subdomain_policy = self.sp
        self.version = self.v
