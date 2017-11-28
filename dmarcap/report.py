"""
dmarclib/report.py - DMARC aggregate report representation.
Ref. https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class Report(object):
    """
    DMARC aggregate report representation
    """
    def __init__(self):
        #: Aggregate report :class:`~dmarcap.meta_data.MetaData`.
        #: Contains information about the reporting organization 
        #: and the report range.
        self.meta_data = None
        #: Aggregate report :class:`~dmarcap.policy_published.PolicyPublished`.
        #: Contains the policy and
        #: reporting values published in DNS by the domain owner. These
        #: were the policies used to evaluate incoming mail.
        self.policy_published = None
        #: List of aggregate report :class:`~dmarcap.record.Record`.
        #: Contains all records from the
        #: aggregate report.
        self.records = []

    def dmarc_failures(self):
        """Returns a list of failed :class:`~dmarcap.record.Record`"""
        if self.records is not None:
            return [record for record
                    in self.records if record.policy_evaluated.spf == "fail"
                    or record.policy_evaluated.dkim == "fail"]
