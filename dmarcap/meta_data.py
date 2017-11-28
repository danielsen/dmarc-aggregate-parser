"""
dmarcap.py/meta_data.py - DMARC aggregate report meta data representation.
Ref. https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
from datetime import datetime

class MetaData(object):
    """
    Representation of aggregate report MetaDataType 
    """
    def __init__(self):
        #: Organization which generated the report
        self.org_name = None
        #: Organzation contact email
        self.email = None
        #: Additional organization contact info
        self.extra_contact_info = None
        #: Unique report id
        self.report_id = None
        #: Report date range beginning (unix timestamp).
        self.date_range_begin = None
        #: Report date range ending (unix timestamp).
        self.date_range_end = None

    def begin_utc_date_iso(self):
        """Returns report begin date in UTC ISO format"""
        return datetime.utcfromtimestamp(
            float(self.date_range_begin)).isoformat()

    def end_utc_date_iso(self):
        """Returns report end date in UTC ISO format"""
        return datetime.utcfromtimestamp(
            float(self.date_range_end)).isoformat()

    def begin_localized_date_iso(self):
        """Return report begin date in localtime ISO format"""
        return datetime.fromtimestamp(
            float(self.date_range_begin)).isoformat()

    def end_localized_date_iso(self):
        """Return report end date in localtime ISO format"""
        return datetime.fromtimestamp(
            float(self.date_range_end)).isoformat()
