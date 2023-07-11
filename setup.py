# coding: utf8
from setuptools import setup

setup(
    name="aioping",
    packages=["aioping"],
    version="0.4.0",
    install_requires=["async_timeout", "aiodns"],
    description="Asyncio ping implementation",
    author="Anton Belousov",
    author_email="anton@belousov.co",
    url="https://github.com/stellarbit/aioping",
    download_url="https://github.com/stellarbit/aioping/tarball/0.4.0",
    keywords=["network", "icmp", "ping", "asyncio"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
