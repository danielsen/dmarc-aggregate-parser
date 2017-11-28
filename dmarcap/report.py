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
        self.records = None
