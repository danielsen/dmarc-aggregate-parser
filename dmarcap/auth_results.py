"""
dmarcap/auth_results.py - DMARC aggregate report AuthResultsType 
representation. Ref. https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class Authentication(object):
    """
    Base class for verification results
    """
    def __init__(self, domain=None, result=None):
        #: Domain name represented in this verification
        self.domain = domain
        #: Verification result
        self.result = result

class DkimAuthentication(Authentication):
    """
    Representation of DkimAuthResultType
    """
    def __init__(self, domain=None, result=None):
        Authentication.__init__(self, domain=domain, result=result)
        #: DKIM selector, e.g. k1, used in authentication
        self.selector = None
        #: Any friendly, human-readable message.
        self.human_result = None

class SpfAuthentication(Authentication):
    """
    Representation of SpfAuthResultType
    """
    def __init__(self, domain=None, result=None):
        Authentication.__init__(self, domain=domain, result=result)
        #: SPF domain scope
        self.scope = None

class AuthResults(object):
    """
    Representation of AuthResultsType
    """
    def __init__(self):
        #: :class:`DkimAuthentication`
        self.dkim = None
        #: :class:`SpfAuthentication`
        self.spf = None
