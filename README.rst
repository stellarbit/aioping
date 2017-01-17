aioping is a fast asyncio implementation of ICMP (ping) protocol.


Installation
------------

aioping requires Python 3.5 and is not yet available on PyPI.
Use pip to install it::

    $ pip install git+https://github.com/stellarbit/aioping


Using aioping
------------

There are 2 ways to use the library.

First one is interactive, which prints results to the stdout.
Please make sure you are running this code under root, as only
root is allowed to send ICMP packets:

.. code:: python

    import asyncio
    import aioping

    loop = asyncio.get_event_loop()
    loop.run_until_complete(aioping.verbose_ping("google.com"))

Alternatively, you can call a ping function, which returns a
ping delay in milliseconds or throws an exception in case of
error:

.. code:: python

    import asyncio
    import aioping

    async def do_ping(host):
        try:
            delay = await aioping.ping(host)
            print("Ping response in %s ms" % delay)

        except TimeoutError:
            print("Timed out")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_ping("google.com"))


Credits
-------

- Original Version from Matthew Dixon Cowles:
  ftp://ftp.visi.com/users/mdc/ping.py

- Rewrite by Jens Diemer:
  http://www.python-forum.de/post-69122.html#69122

- Rewrite by Samuel Stauffer:
  https://github.com/samuel/python-ping

- Rewrite by Anton Belousov / Stellarbit LLC <anton@stellarbit.com>
  http://github.com/stellarbit/aioping


License
-------

aioping is licensed under GPLv2.
