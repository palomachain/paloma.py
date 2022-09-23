import asyncio
import base64
from pathlib import Path

from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.core import Coins
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.core.tx import SignMode
from paloma_sdk.key.mnemonic import MnemonicKey


def main():
    paloma = LCDClient(
        url="http://localhost:1317/",
        chain_id="localpaloma",
    )
    key = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )
    test1 = paloma.wallet(key=key)

    msg = MsgSend(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(uluna=20000),
    )
    print(msg)
    tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[msg],
            gas_prices="0.15uluna",
            gas="63199",  # gas="auto", gas_adjustment=1.1
        )
    )
    print(tx)

    result = paloma.tx.broadcast_async(tx)
    print(result)


main()
