import asyncio
import uvloop
from pathlib import Path
from terra_proto.cosmwasm.wasm.v1 import AccessType

from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.client.lcd.params import PaginationOptions
from paloma_sdk.key.mnemonic import MnemonicKey
from paloma_sdk.client.lcd.api.tx import Tx, CreateTxOptions, SignerOptions
from paloma_sdk.core.wasm import MsgInstantiateContract, MsgExecuteContract, MsgStoreCode
from paloma_sdk.core.wasm.data import AccessConfig
from paloma_sdk.util.contract import get_code_id, get_contract_address, read_file_as_b64

paloma = AsyncLCDClient(url="http://localhost:1317", chain_id="localpaloma")
paloma.gas_prices = "1ugrain"
pagOpt = PaginationOptions(limit=2, count_total=True)

mk = MnemonicKey(
    mnemonic="nut praise glare false post crane clinic nothing happy effort loyal point parent few series task base maximum insect glass twice inflict tragic cancel"
)

mk2 = MnemonicKey(
    mnemonic="nut praise glare false post crane clinic nothing happy effort loyal point parent few series task base maximum insect glass twice inflict tragic cancel"
)

def test_cw20():
    wallet = paloma.wallet(mk)
    wasm_bytecode = read_file_as_b64(Path(__file__).parent / "./cw20_base.wasm")
    store_code_tx = wallet.create_and_sign_tx(CreateTxOptions(
        msgs=[MsgStoreCode(
            wallet.key.acc_address,
            wasm_bytecode,
            AccessConfig(AccessType.ACCESS_TYPE_EVERYBODY, ""),
        )],
        gas_adjustment=1.75,
    ))
    store_code_tx_result = paloma.tx.broadcast(store_code_tx)
    print(store_code_tx_result)
    code_id = get_code_id(store_code_tx_result)
    print(f"code_id:{code_id}")
    code_id = 100
    result = paloma.cw20.instantiate(wallet,
                                   code_id,
                                   "CW20 Token",
                                   "CW20",
                                   9,
                                   1_000_000_000_000_000
                                   )
    contract_address = get_contract_address(result)
    print(contract_address)
    wallet2 = paloma.wallet(mk2)
    result = paloma.cw20.transfer(wallet,
                                contract_address,
                                wallet.key.acc_address,
                                1_000_000_000
                                )

uvloop.install()
asyncio.run(test_cw20())