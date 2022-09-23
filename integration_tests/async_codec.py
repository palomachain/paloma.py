import asyncio

import uvloop

from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.core import Coins
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.key.mnemonic import MnemonicKey


async def with_sem(aw, sem):
    async with sem:
        print(sem)
        return await aw


async def main():
    paloma = AsyncLCDClient(chain_id="pisco-1", url="https://pisco-lcd.paloma.dev/")
    mk = MnemonicKey(
        mnemonic="index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred"
    )
    awallet = paloma.wallet(mk)

    msg = MsgSend(
        "paloma1333veey879eeqcff8j3gfcgwt8cfrg9mq20v6f",
        "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(uluna=20),
    )
    tx = await awallet.create_and_sign_tx(
        CreateTxOptions(
            msgs=[msg],
            gas_prices="0.15uluna",
            gas="63199",  # gas="auto", gas_adjustment=1.1
            fee_denoms=["uluna"],
        )
    )

    encoded = await paloma.tx.encode(tx)
    print(f"encoded...{encoded}")

    print("=" * 64)

    decoded = await paloma.tx.decode(encoded)
    print(f"decoded...{decoded}")

    await paloma.session.close()


uvloop.install()
asyncio.run(main())
