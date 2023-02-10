import asyncio
from pathlib import Path

import uvloop
from terra_proto.cosmwasm.wasm.v1 import AccessType
from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.core.wasm import MsgInstantiateContract, MsgStoreCode
from paloma_sdk.key.mnemonic import MnemonicKey
from paloma_sdk.core.wasm.data import AccessConfig
from paloma_sdk.util.contract import get_code_id, get_contract_address, read_file_as_b64


async def main():
    paloma = AsyncLCDClient(url="https://lcd.testnet.palomaswap.com/", chain_id="paloma-testnet-15")
    paloma.gas_prices = "0.01ugrain"

    acc = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    acc2 = MnemonicKey(
        mnemonic="index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred"
    )
    test1 = paloma.wallet(acc)
    test2 = paloma.wallet(acc2)

    job_id = "testjob0"
    contract_address = "0x1f576F2021b6EBdF229750f54fDFd31206141E65"
    abi = [{"inputs":[],"name":"retrieve","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"num","type":"uint256"}],"name":"store","outputs":[],"stateMutability":"nonpayable","type":"function"}]
    payload = "6057361d00000000000000000000000000000000000000000000000000000000000000ea"
    chain_type = "evm"
    chain_reference_id = "bnb-main"
    result = await paloma.job_scheduler.create_job(
        test1, job_id, contract_address, abi, payload, chain_type, chain_reference_id
    )
    print(result)
    
    # contract_address = result.logs[0].events_by_type["instantiate"][
    #         "_contract_address"
    #     ][0]
    # print(contract_address)

    # result = await paloma.cw20.transfer(
    #     test1, contract_address, test2.key.acc_address, 1_000_000_000
    # )
    # print(result)

    # result = await paloma.cw20.burn(
    #     test1, contract_address, 500_000_000
    # )
    # print(result)

    await paloma.session.close()


uvloop.install()
asyncio.run(main())
