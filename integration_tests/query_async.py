import asyncio
import base64
from pathlib import Path

import uvloop

from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.core import Coins
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.util.contract import get_code_id


async def main():
    paloma = AsyncLCDClient(
        url="https://pisco-lcd.paloma.dev/",
        chain_id="pisco-1",
    )

    result = await paloma.tx.tx_infos_by_height(None)
    print(result)


uvloop.install()
asyncio.run(main())
