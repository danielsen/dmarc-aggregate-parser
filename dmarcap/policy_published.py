"""
dmarcap/policy_published.py - DMARC aggregate report published policy
representation. Ref. https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class PolicyPublished(object):
    """Representation of PolicyPublishedType"""
    def __init__(self):
        #: Domain publishing this policy
        self.domain = None
        #: Dkim authentication mode
        self.adkim = None
        #: Spf authentication mode
        self.aspf = None
        #: Failure reporting options
        self.fo = None
        #: DMARC policy
        self.p = None
        #: Policy percent, i.e. what percent of mail stream to
        #: apply the published policy to.
        self.pct = None
        #: Preferred report format
        self.rf = None
        #: Preferred report interval
        self.ri = None
        #: Aggregate report delivery URI
        self.rua = None
        #: Forensic report delivery URI
        self.ruf = None
        #: Sub domain policy
        self.sp = None
        #: DMARC version
        self.v = None
        #: Long format accessor for :attr:`fo`
        self.failure_reporting_options = self.fo
        #: Long format accessor for :attr:`p`
        self.policy = self.p
        #: Long format accessor for :attr:`pct`
        self.percent = self.pct
        #: Long format accessor for :attr:`rf`
        self.report_format = self.rf
        #: Long format accessor for :attr:`ri`
        self.report_interval = self.ri
        #: Long format accessor for :attr:`rua`
        self.report_uri_aggregate = self.rua
        #: Long format accessor for :attr:`ruf`
        self.report_uri_forensic = self.ruf
        #: Long format accessor for :attr:`sp`
        self.subdomain_policy = self.sp
        #: Long format accessor for :attr:`v`
        self.version = self.v
