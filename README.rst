aioping is a fast asyncio implementation of ICMP (ping) protocol.


Installation
------------

aioping requires Python 3.5. 

Use pip to install it from the PyPI::

    $ pip install aioping

Or use the latest version from the master (if you are brave enough)::

    $ pip install git+https://github.com/stellarbit/aioping

Using aioping
-------------

There are 3 ways to use the library.

First one is interactive, which sends results to standard Python logger.
Please make sure you are running this code under root, as only
root is allowed to send ICMP packets:

.. code:: python

    import asyncio
    import aioping
    import logging

    logging.basicConfig(level=logging.INFO)     # or logging.DEBUG
    asyncio.run(aioping.verbose_ping("google.com"))

Secondly, you can call a ping function, which returns a
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

    asyncio.run(do_ping("google.com"))
    
The last way is to call a multiping function, which returns a
list of tuples. The tuples are formatted as (dest_addr, delay) with 
delay measured in milliseconds. In the event of a timeout, the tuple 
will be returned as (dest_addr, 'TimeoutError'). Lowering the timeout 
will result in a faster return. NOTE: This function is limited to 255
pings at one time due to the limitation of select().

.. code:: python

    import asyncio
    import aioping
    
    async def do_multiping():
        results = await aioping.multiping(['8.8.8.8','1.1.1.1','google.com'])
        print(results)
        
    asyncio.run(do_multiping())

Methods
-------

``ping(dest_addr, timeout=10, family=None)``

- ``dest_addr`` - destination address, IPv4, IPv6 or hostname
- ``timeout`` - timeout in seconds (default: ``10``)
- ``family`` - family of resolved address - ``socket.AddressFamily.AF_INET`` for IPv4, ``socket.AddressFamily.AF_INET6``
  for IPv6 or ``None`` if it doesn't matter (default: ``None``)

``verbose_ping(dest_addr, timeout=2, count=3, family=None)``

- ``dest_addr`` - destination address, IPv4, IPv6 or hostname
- ``timeout`` - timeout in seconds (default: ``2``)
- ``count`` - count of packets to send (default: ``3``)
- ``family`` - family of resolved address - ``socket.AddressFamily.AF_INET`` for IPv4, ``socket.AddressFamily.AF_INET6``
  for IPv6 or ``None`` if it doesn't matter (default: ``None``)
  
``multiping(dest_addr, timeout=5, family=None)``

- ``dest_addr`` - destination address, IPv4, IPv6 or hostname
- ``timeout`` - timeout in seconds (default: ``5``)
- ``family`` - family of resolved address - ``socket.AddressFamily.AF_INET`` for IPv4, ``socket.AddressFamily.AF_INET6``
  for IPv6 or ``None`` if it doesn't matter (default: ``None``)

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
  
- Generous contributions from GitHub users:

  - https://github.com/JackSlateur
  - https://github.com/harriv
  - https://github.com/asantoni
  - https://github.com/eddebc
  - https://github.com/wise0wl
  - https://github.com/nARN
  - https://github.com/hergla
  - https://github.com/hanieljgoertz
  - https://github.com/Crypto-Spartan


License
-------

aioping is licensed under GPLv2.
