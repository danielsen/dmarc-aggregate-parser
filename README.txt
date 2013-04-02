dmarclib-0.7

-------------------------------------------------------------------------------
Introduction

dmarclib provides an abstraction of DMARC aggregate reports as defined at
http://dmarc.org/draft-dmarc-base-00-02.txt.

REQUIRES: Python2.7+

-------------------------------------------------------------------------------
Installation

The dmarclib module is shipped as a distutils package. To install the library
unpack the distribution archive and run:

	$ python setup.py install

-------------------------------------------------------------------------------
Usage:

Two convenience functions are provided for generating reports.

	dmarc_report = dmarclib.report.report_from_email(email_as_string)
	dmarc_report = dmarclib.report.report_from_file(file_path, zipped=T/F)

Alternatively:
	dmarc_report = dmarclib.report.Report(dmarc_xml_as_string)
