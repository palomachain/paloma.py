import asyncio

import uvloop

from paloma_sdk.client.lcd import AsyncLCDClient


async def with_sem(aw, sem):
    async with sem:
        print(sem)
        return await aw


async def main():
    paloma = AsyncLCDClient(url="https://lcd.testnet.palomaswap.com", chain_id="pisco-1")
    validators, _ = await paloma.staking.validators()
    validator_addresses = [v.operator_address for v in validators]

    sem = asyncio.Semaphore(2)  # 2 continuous connections
    result = await asyncio.gather(
        *[
            with_sem(paloma.oracle.misses(address), sem)
            for address in validator_addresses
        ]
    )

    await paloma.session.close()
    print(result)


uvloop.install()
asyncio.run(main())
