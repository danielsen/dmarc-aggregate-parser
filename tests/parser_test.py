"""unit tests for Parser class"""
import unittest
import sys
sys.path.insert(0, "./")
import dmarcap
from datetime import datetime

class ParserTestFixture(unittest.TestCase):
    """Parser class test fixture"""

    def setUp(self):
        self.report_xml = "./tests/sample_report.xml"
        self.invalid_xml = "./tests/invalid_report.xml"
        self.parser = dmarcap.Parser(self.report_xml)
        self.invalid_parser = dmarcap.Parser(self.invalid_xml)

    def test_meta_data(self):
        """Tests for the MetaData class parsing"""
        meta_data = self.parser.parse_meta_data()

        self.assertEqual(meta_data.org_name, "Yahoo! Inc.")
        self.assertEqual(meta_data.email, "postmaster@dmarc.yahoo.com")
        self.assertEqual(meta_data.report_id, "1486092501.419151")
        self.assertEqual(meta_data.date_range_begin, "1485993600")
        self.assertEqual(meta_data.date_range_end, "1486079999")
        self.assertEqual(meta_data.extra_contact_info, None)
        self.assertEqual(meta_data.begin_utc_date_iso(), datetime.utcfromtimestamp(
            float(1485993600)).isoformat())
        self.assertEqual(meta_data.end_utc_date_iso(), datetime.utcfromtimestamp(
            float(1486079999)).isoformat())
        self.assertEqual(meta_data.begin_localized_date_iso(), datetime.fromtimestamp(
            float(1485993600)).isoformat())
        self.assertEqual(meta_data.end_localized_date_iso(), datetime.fromtimestamp(
            float(1486079999)).isoformat())

    def test_policy_published(self):
        """Tests for the PolicyPublished class parsing"""
        policy_published = self.parser.parse_policy_published()

        self.assertEqual(policy_published.domain, "acme-company.net")
        self.assertEqual(policy_published.adkim, "r")
        self.assertEqual(policy_published.aspf, "r")
        self.assertEqual(policy_published.p, "none")
        self.assertEqual(policy_published.pct, "100")

    def test_records(self):
        """Tests for parsing report records"""
        records = self.parser.parse_report_records()

        self.assertEqual(len(records), 1)

        first_record = records[0]
        self.assertEqual(first_record.count, "1")
        self.assertEqual(first_record.source_ip, "62.149.157.24")
        self.assertEqual(first_record.policy_evaluated.disposition, "none")
        self.assertEqual(first_record.policy_evaluated.dkim, "fail")
        self.assertEqual(first_record.policy_evaluated.spf, "fail")
        self.assertEqual(first_record.identifiers.header_from, "mail6.acme-company.net")
        self.assertEqual(first_record.identifiers.envelope_to, None)
        self.assertEqual(first_record.identifiers.envelope_from, None)
        self.assertEqual(first_record.auth_results.dkim.domain, "mail6.acme-company.net")
        self.assertEqual(first_record.auth_results.dkim.result, "neutral")
        self.assertEqual(first_record.auth_results.dkim.selector, None)
        self.assertEqual(first_record.auth_results.dkim.human_result, None)
        self.assertEqual(first_record.auth_results.spf.domain, "mail6.acme-company.net")
        self.assertEqual(first_record.auth_results.spf.result, "softfail")

    def test_failures(self):
        """Tests identification of dmarc failures"""
        aggregate_report = self.parser.parse_report()
        failures = aggregate_report.dmarc_failures()

        self.assertEqual(len(failures), 1)

    def test_invalid_meta_data(self):
        """Test for invalid xml metadata"""
        meta_data = self.invalid_parser.parse_meta_data()

        self.assertEqual(meta_data, None)

    def test_invalid_policy_published(self):
        """Test for invalid xml policy published"""
        policy_published = self.invalid_parser.parse_policy_published()

        self.assertEqual(policy_published, None)

    def test_full_report_parse(self):
        """Test full report parsing"""
        aggregate_report = self.parser.parse_report()

        self.assertNotEqual(aggregate_report.meta_data, None)
        self.assertNotEqual(aggregate_report.policy_published, None)
        self.assertEqual(len(aggregate_report.records), 1)

if __name__ == "__main__":
    unittest.main()
