"""
dmarclib.py/meta_data.py - Abstract representation of the meta_data node
from a DMARC aggregate XML report. For more information, refer to the
XML schema at https://tools.ietf.org/html/rfc7489#appendix-C
"""
from builtins import object
from datetime import datetime

class MetaData(object):
    """
    Representation of aggregate report meta_data
    """
    def __init__(self):
        self.org_name = None
        self.email = None
        self.extra_contact_info = None
        self.report_id = None
        self.date_range_begin = None
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
