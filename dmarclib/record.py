"""
dmarclib/record.py - Representation of a record in a DMARC XML aggregate
report. For more information, refer to
https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class Record(object):
    """Representation of an aggregate report record"""
    def __init__(self):
        self.source_ip = None
        self.count = None
        self.indentifiers = None
        self.auth_results = None
        self.policy_evaluated = None
