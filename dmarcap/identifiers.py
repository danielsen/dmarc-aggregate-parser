"""
dmarcap/identifiers/py - DMARC aggregate report IdentifierType representation
Ref. https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
class Identifiers(object):
    """
    Represention of the aggregate record IdentifierType
    """
    def __init__(self):
        #: From header field of the evaluated message
        self.header_from = None
        #: Envelope recipient of the SMTP transaction.
        #: E.g ``RCPT TO: <jane@example.com>``
        self.envelope_to = None
        #: Envelope from of the evaluated message or
        #: SMTP transaction. E.g. ``MAIL FROM:<errors@example.com>``
        #: or ``Return-Path: <errors@example.com>``
        self.envelope_from = None
