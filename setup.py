from distutils.core import setup

setup(
    name="dmarclib",
    version="1.0",
    license="MIT",
    author="Dan Nielsen",
    author_email="dnielsen@reachmail.com",
    url="https://github.com/danielsen/dmarclib.git",
    packages=["dmarclib"],
    install_requires=[
        "defusedxml",
        "future"
    ]
)
