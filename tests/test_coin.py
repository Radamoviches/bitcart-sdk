"""Test that Coin class methods are abstract, and test module loading
coin fixture is the abstract coin class tested
"""
import pytest

pytestmark = pytest.mark.asyncio


async def test_help(coin):
    with pytest.raises(NotImplementedError):
        await coin.help()

async def test_get_tx(coin):
    with pytest.raises(NotImplementedError):
        await coin.get_tx("")

async def test_get_address(coin):
    with pytest.raises(NotImplementedError):
        await coin.get_address("")

async def test_balance(coin):
    with pytest.raises(NotImplementedError):
        await coin.balance()
        