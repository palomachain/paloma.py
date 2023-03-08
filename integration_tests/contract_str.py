from pathlib import Path

from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.client.localpaloma import LocalPaloma
from paloma_sdk.core import Coins
from paloma_sdk.core.fee import Fee
from paloma_sdk.core.wasm import (
    MsgExecuteContract,
    MsgInstantiateContract,
    MsgStoreCode,
)
from paloma_sdk.util.contract import get_code_id, get_contract_address, read_file_as_b64


def main():
    paloma = LocalPaloma()
    paloma.gas_prices = "1ugrain"
    test1 = paloma.wallets["test1"]

    store_code_tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[
                MsgStoreCode(
                    test1.key.acc_address,
                    read_file_as_b64(Path(__file__).parent / "./strtest.wasm"),
                )
            ],
            gas_adjustment=1.75,
        )
    )
    store_code_tx_result = paloma.tx.broadcast(store_code_tx)
    print(store_code_tx_result)

    code_id = get_code_id(store_code_tx_result)
    print(f"cod_id:{code_id}")

    instantiate_tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[
                MsgInstantiateContract(
                    test1.key.acc_address, test1.key.acc_address, code_id, "test_init"
                )
            ],
            gas_prices="10ugrain",
            gas_adjustment=2,
        )
    )
    print(instantiate_tx)
    instantiate_tx_result = paloma.tx.broadcast(instantiate_tx)
    print(instantiate_tx_result)
    contract_address = get_contract_address(instantiate_tx_result)
    # """
    # contract_address = "paloma1e8d3cw4j0k5fm9gw03jzh9xzhzyz99pa8tphd8"
    result = paloma.wasm.contract_query(contract_address, "count")
    print("get_count1: ", result)
    execute_tx = test1.create_and_sign_tx(
        CreateTxOptions(
            msgs=[
                MsgExecuteContract(test1.key.acc_address, contract_address, "increment")
            ],
            gas_adjustment=1.75,
        )
    )
    #                {"ugrain": 1000},

    execute_tx_result = paloma.tx.broadcast(execute_tx)
    print(execute_tx_result)

    result = paloma.wasm.contract_query(contract_address, "count")
    print("get_count2: ", result)
    result = paloma.wasm.contract_query(contract_address, "test")
    print("get_test: ", result)


# try:
main()
# except Exception as e:
#    print("exception occured")
#    print(e)
