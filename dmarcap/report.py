"""
dmarclib/report.py - Abstract representation of a DMARC aggregate report
"""
from builtins import object
class Report(object):
    """
    Abstract representation of a DMARC aggregate report
    """
    def __init__(self):
        self.meta_data = None
        self.policy_published = None
        self.records = []

    def dmarc_failures(self):
        """Returns a list of failed records"""
        if self.records is not None:
            return [record for record
                    in self.records if record.policy_evaluated.spf == "fail"
                    or record.policy_evaluated.dkim == "fail"]
