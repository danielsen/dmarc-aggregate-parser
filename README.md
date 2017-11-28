# dmarc-aggregate-parser (dmarcap)

![License MIT](https://img.shields.io/npm/l/express.svg?style=for-the-badge) ![Python Versions 2.7 3.4 3.5 3.6](https://img.shields.io/badge/python-2.7%203.4%203.5%203.6-brightgreen.svg?style=for-the-badge)

dmarcap provides a simple python parser for DMARC aggregate reports as defined
in https://tools.ietf.org/html/rfc7489

### Installation

dmarcap is shipped as a distutils package. To install, clone the repository and run:

    $ python setup.py install

### Usage

To parse an aggregate report:

    >>> import dmarcap
    >>> aggregate_report = dmarcap.Parser("/path/to/report.xml").parse_report()
