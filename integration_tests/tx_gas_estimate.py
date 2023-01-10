import asyncio
from pathlib import Path

import uvloop
from terra_proto.cosmwasm.wasm.v1 import AccessType
from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.core.wasm import MsgInstantiateContract, MsgStoreCode
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.core import Coins
from paloma_sdk.core.fee import Fee
from paloma_sdk.key.mnemonic import MnemonicKey
from paloma_sdk.core.wasm.data import AccessConfig
from paloma_sdk.util.contract import get_code_id, get_contract_address, read_file_as_b64


async def main():
    paloma = AsyncLCDClient(url="https://lcd.testnet.palomaswap.com/", chain_id="paloma-testnet-13")
    paloma.gas_prices = "1ugrain"
    acc = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    test = paloma.wallet(acc)

    code_id = 49
    instantiate_msg = {
        "name": "CW20 Token",
        "symbol": "CWFT",
        "decimals": 9,
        "initial_balances": [
            {
                "address": test.key.acc_address,
                "amount": str(1_000_000_000_000_000)
            }
        ]
    }
    funds = Coins.from_str("0ugrain")
    tx = await test.create_and_sign_tx(CreateTxOptions(
        msgs=[MsgInstantiateContract(
            test.key.acc_address,
            None,
            code_id,
            "CW20",
            instantiate_msg,
            funds
        )],
        fee=Fee(10000000, "10000000ugrain")
    ))
    result = await paloma.tx.broadcast(tx)
    print(result)
    await paloma.session.close()


uvloop.install()
asyncio.run(main())
