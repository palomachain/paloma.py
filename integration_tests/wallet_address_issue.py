import asyncio
from pathlib import Path

import uvloop
from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.key.mnemonic import MnemonicKey


async def main():
    paloma = AsyncLCDClient(url="https://lcd.testnet.palomaswap.com/", chain_id="paloma-testnet-13")
    acc = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )
    test = paloma.wallet(acc)
    print(test.key.acc_address)

    await paloma.session.close()


uvloop.install()
asyncio.run(main())
