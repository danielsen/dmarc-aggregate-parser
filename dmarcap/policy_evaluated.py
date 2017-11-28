"""
dmarclib/policy_evaluated.py - Repsentation of the policy_evaluated node
of a DMARC aggregate report record. For more information, refer to
https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class PolicyEvaluated(object):
    """Representation of policy_evaluated"""
    def __init__(self):
        self.disposition = None
        self.dkim = None
        self.spf = None
