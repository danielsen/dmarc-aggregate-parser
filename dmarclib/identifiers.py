"""
dmarclib/identifiers/py - Abstract representation of the identifiers node
in a DMARC aggregate report. For more information, refer the XML schema
at https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class Identifiers(object):
    """
    Represention of the aggregate record IdentifierType
    """
    def __init__(self):
        self.header_from = None
        self.envelope_to = None
        self.envelope_from = None
