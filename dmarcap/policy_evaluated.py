"""
dmarcap/policy_evaluated.py - DMARC aggregate report evaluation policy
representation. Ref. https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class PolicyEvaluated(object):
    """Representation of PolicyEvaluatedType"""
    def __init__(self):
        #: Disposition of the :class:`~dmarcap.record.Record`
        self.disposition = None
        #: Dkim result for the :class:`~dmarcap.record.Record`
        self.dkim = None
        #: Spf result for the :class:`~dmarcp.record.Record`
        self.spf = None
