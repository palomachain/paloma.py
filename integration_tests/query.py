import asyncio
import base64
from pathlib import Path

from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.core import Coins
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.util.contract import get_code_id


def main():
    paloma = LCDClient(
        url="https://lcd.testnet.palomaswap.com/",
        chain_id="pisco-1",
    )

    result = paloma.tx.tx_infos_by_height(None)
    print(result)


main()
