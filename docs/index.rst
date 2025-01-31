.. Bitcart SDK documentation master file, created by
   sphinx-quickstart on Tue Jul  9 22:11:54 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Bitcart SDK's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   api

Bitcart is a platform to simplify cryptocurrencies adaptation.
This SDK is part of bitcart.
Using this SDK you can easily connect to bitcart daemon
and code scripts around it easily.

Behold, the power of Bitcart:

.. code-block:: python

    from bitcart.coins.btc import BTC

    btc = BTC(xpub="your x/y/zpub or x/y/zprv")


    @btc.on("new_transaction")
    def callback_func(event, tx):
        print(event)
        print(tx)


    btc.poll_updates()

This simple script will listen for any new transaction on your
wallet's addresses and print information about them like so:

.. image:: images/1.png

And if you add ``print(btc.get_tx(tx))`` it would print
full information about every transaction, too!

To run this script, refer to :doc:`installation <installation>` section.
For examples of usage, check examples directory in github repository.

Supported coins list(⚡ means lightning is supported):

- Bitcoin (⚡)
- Litecoin (⚡)
- Gravity Zero (⚡)
