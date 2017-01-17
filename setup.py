# coding: utf8
from distutils.core import setup

setup(
    name="aioping",
    packages=["aioping"],
    version="0.1.0",
    description="Asyncio ping implementation",
    author="Anton Belousov",
    author_email="anton@stellarbit.com",
    url="https://github.com/stellarbit/aioping",
    download_url="https://github.com/stellarbit/aioping/tarball/0.1.0",
    keywords=["network", "icmp", "ping", "asyncio"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
