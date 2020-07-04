from unittest import TestCase
import asyncio
from aioping import verbose_ping, ping
import logging


class TestAioping(TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        logging.basicConfig(level=logging.DEBUG)

    def test_verbose_ping(self):
        loop = asyncio.get_event_loop()

        tasks = [
            asyncio.ensure_future(verbose_ping("heise.de")),
            asyncio.ensure_future(verbose_ping("google.com")),
            asyncio.ensure_future(verbose_ping("a-test-url-taht-is-not-available.com")),
            asyncio.ensure_future(verbose_ping("192.168.1.111"))
        ]

        loop.run_until_complete(asyncio.gather(*tasks))

    async def _do_ping(self, host):
        try:
            delay = await ping(host) * 1000
            print("Ping response from %s in %s ms" % (host, delay))
        except TimeoutError:
            print("Timed out")

    def test_ping(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._do_ping("192.168.0.255"))
