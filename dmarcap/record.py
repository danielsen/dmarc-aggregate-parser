"""
dmarcap/record.py - DMARC aggregate report RecordType representation.
Ref. https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class Record(object):
    """Representation of an aggregate report record"""
    def __init__(self):
        #: IP traffic source
        self.source_ip = None
        #: Number of messages received from this IP
        self.count = None
        #: Message or SMTP :class:`~dmarcap.identifiers.Identifiers`
        self.identifiers = None
        #: Message :class:`~dmarcap.auth_results.AuthResults`
        self.auth_results = None
        #: Message :class:`~dmarcap.policy_evaluated.PolicyEvaluated`
        self.policy_evaluated = None
