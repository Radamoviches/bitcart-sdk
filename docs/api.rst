API Reference
=============

Coin class
**********

.. autoclass:: bitcart.coin.Coin
    :members:
    :show-inheritance:
    :undoc-members:

Implemented coins
*****************

BTC
---

BTC class supports lightning out of the box.
For lightning methods to work, it must be enabled from the daemon
(enabled by default and edited by ``BTC_LIGHTNING`` environment variable).
If lightning is disabled, ``LightningDisabledError`` is raised when
calling lightning methods.

.. autoclass:: bitcart.coins.btc.BTC
    :members:
    :show-inheritance:
    :undoc-members:

LTC
---

LTC class supports lightning out of the box.
For lightning methods to work, it must be enabled from the daemon
(enabled by default and edited by ``LTC_LIGHTNING`` environment variable).
If lightning is disabled, ``LightningDisabledError`` is raised when
calling lightning methods.

.. autoclass:: bitcart.coins.ltc.LTC
    :members:
    :show-inheritance:
    :undoc-members:

GZRO
----

GZRO class supports lightning out of the box.
For lightning methods to work, it must be enabled from the daemon
(enabled by default and edited by ``GZRO_LIGHTNING`` environment variable).
If lightning is disabled, ``LightningDisabledError`` is raised when
calling lightning methods.

.. autoclass:: bitcart.coins.gzro.GZRO
    :members:
    :show-inheritance:
    :undoc-members:
