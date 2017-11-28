"""
dmarclib/auth_results.py - Abstract classes used for representing the
auth_results node in an aggregate report record.
For more information, see the XML schema at
https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class Authentication(object):
    """
    Base class for verification results
    """
    def __init__(self, domain=None, result=None):
        self.domain = domain
        self.result = result

class DkimAuthentication(Authentication):
    """
    Representation of DkimAuthResultType
    """
    def __init__(self, domain=None, result=None):
        Authentication.__init__(self, domain=domain, result=result)
        self.selector = None
        self.human_result = None

class SpfAuthentication(Authentication):
    """
    Representation of SpfAuthResultType
    """
    def __init__(self, domain=None, result=None):
        Authentication.__init__(self, domain=domain, result=result)
        self.scope = None

class AuthResults(object):
    """
    Representation of AuthResultsType
    """
    def __init__(self):
        self.dkim = None
        self.spf = None
