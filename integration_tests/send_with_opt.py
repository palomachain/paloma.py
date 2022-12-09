import asyncio
import base64
from pathlib import Path

from paloma_sdk.client.lcd.api.tx import BroadcastOptions
from paloma_sdk.client.localpaloma import LocalPaloma
from paloma_sdk.core import Coins
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.util.contract import get_code_id


def main():
    paloma = LocalPaloma()
    test1 = paloma.wallets["test1"]

    print(test1)
    msg = MsgSend(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(ugrain=1000000),
    )
    print(msg)
    tx = test1.create_and_sign_tx(msgs=[msg])
    print(tx)

    opt = BroadcastOptions(
        sequences=[58], fee_granter="paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v"
    )

    result = paloma.tx.broadcast(tx, opt)
    print(result)


main()
