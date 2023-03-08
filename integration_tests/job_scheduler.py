import asyncio

import uvloop

from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.key.mnemonic import MnemonicKey


async def main():
    paloma = AsyncLCDClient(
        url="https://lcd.testnet.palomaswap.com/", chain_id="paloma-testnet-15"
    )
    paloma.gas_prices = "0.01ugrain"

    acc = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    test1 = paloma.wallet(acc)

    job_id = "test100"
    contract_address = "0x1f576F2021b6EBdF229750f54fDFd31206141E65"
    abi = [
        {
            "inputs": [],
            "name": "retrieve",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "num", "type": "uint256"}],
            "name": "store",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    payload = "6057361d00000000000000000000000000000000000000000000000000000000000000ea"
    chain_type = "evm"
    chain_reference_id = "bnb-main"
    result = await paloma.job_scheduler.create_job(
        test1, job_id, contract_address, abi, payload, chain_type, chain_reference_id
    )
    print(result)

    job_id = "test100"
    payload = "6057361d0000000000000000000000000000000000000000000000000000000000000003"
    result = await paloma.job_scheduler.execute_job(test1, job_id, payload)
    print(result)
    await paloma.session.close()


uvloop.install()
asyncio.run(main())
