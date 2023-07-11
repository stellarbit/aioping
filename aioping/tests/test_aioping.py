from unittest import TestCase
import asyncio
from aioping import verbose_ping, ping
import logging
import socket


class TestAioping(TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        logging.basicConfig(level=logging.INFO)

    def test_verbose_ping(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        tasks = [
            asyncio.ensure_future(verbose_ping("a-test-url-taht-is-not-available.com"), loop=loop),
            asyncio.ensure_future(verbose_ping("192.168.1.111"), loop=loop),
            asyncio.ensure_future(verbose_ping("heise.de", family=socket.AddressFamily.AF_INET), loop=loop),
            asyncio.ensure_future(verbose_ping("google.com", family=socket.AddressFamily.AF_INET), loop=loop),
            asyncio.ensure_future(verbose_ping("heise.de", family=socket.AddressFamily.AF_INET6), loop=loop),
            asyncio.ensure_future(verbose_ping("google.com", family=socket.AddressFamily.AF_INET6), loop=loop)
        ]

        loop.run_until_complete(asyncio.gather(*tasks))

    async def _do_ping(self, host):
        try:
            delay = await ping(host) * 1000
            print("%s ping response in %0.4fms" % (host, delay))
        except TimeoutError:
            print("%s timed out" % host)

    def test_many_pings(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        tasks = []

        for i in range(255):
            tasks.append(asyncio.ensure_future(self._do_ping("192.168.0.%s" % i), loop=loop))

        loop.run_until_complete(asyncio.gather(*tasks))
