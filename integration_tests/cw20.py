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
    paloma = AsyncLCDClient(url="https://lcd.testnet.palomaswap.com/", chain_id="paloma-testnet-13")
    paloma.gas_prices = "1ugrain"
    # test1 = paloma.wallets["test1"]
    acc = MnemonicKey(
        mnemonic="rotice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    acc2 = MnemonicKey(
        mnemonic="index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred"
    )
    test1 = paloma.wallet(acc)
    test2 = paloma.wallet(acc2)

    # store_code_tx = await test1.create_and_sign_tx(
    #     CreateTxOptions(
    #         msgs=[
    #             MsgStoreCode(
    #                 test1.key.acc_address,
    #                 read_file_as_b64(Path(__file__).parent / "./cw20_base.wasm"),
    #                 AccessConfig(AccessType.ACCESS_TYPE_EVERYBODY, ""),
    #             )
    #         ],
    #         gas_adjustment=1.75,
    #     )
    # )
    # store_code_tx_result = await paloma.tx.broadcast(store_code_tx)
    # print(store_code_tx_result)

    # code_id = get_code_id(store_code_tx_result)
    code_id = 49
    print(f"code_id:{code_id}")

    # instantiate_tx = await test1.create_and_sign_tx(
    #     CreateTxOptions(
    #         msgs=[
    #             MsgInstantiateContract(
    #                 test1.key.acc_address, test1.key.acc_address, code_id, "CW20", {"count": 10}, "0ugrain",
    #             )
    #         ],
    #         gas_prices="1ugrain",
    #         gas_adjustment=2,
    #     )
    # )

    result = await paloma.cw20.instantiate(
        test1, code_id, "CW20 Token", "CW20", 9, 1_000_000_000_000_000, gas_limit=100000, amount="100000ugrain"
    )
    print(result)
    contract_address = get_contract_address(result)

    await paloma.cw20.transfer(
        test1, contract_address, test2.key.acc_address, 1_000_000_000
    )
    
    await paloma.session.close()


uvloop.install()
asyncio.run(main())
