from distutils.core import setup

setup(
    name="dmarcap",
    version="1.0",
    license="MIT",
    author="Dan Nielsen",
    author_email="dnielsen@reachmail.com",
    url="https://github.com/danielsen/dmarc-aggregate-parser.git",
    packages=["dmarcap"],
    install_requires=[
        "defusedxml",
        "future"
    ]
)
