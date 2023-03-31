""" done
import lcd_auth
import lcd_authz
import lcd_bank
import lcd_distribution
import lcd_gov
import lcd_mint
import lcd_slashing
import lcd_wasm
import lcd_tendermint
import lcd_ibc
import lcd_ibc_transfer

"""

from paloma_sdk.client.lcd import LCDClient

# import lcd_tx
from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.client.localpaloma import LocalPaloma
from paloma_sdk.core.bank import MsgMultiSend, MsgSend, MultiSendInput, MultiSendOutput
from paloma_sdk.core.tx import SignMode
from paloma_sdk.key.mnemonic import MnemonicKey
from paloma_sdk.util.json import JSONSerializable

""" untested
import lcd_gov
"""

########

from paloma_sdk.core import Coin, Coins
from paloma_sdk.core.public_key import SimplePublicKey


def main():
    paloma = LCDClient(
        url="https://lcd.testnet.palomaswap.com/",
        chain_id="paloma-testnet-15",
    )
    paloma = LocalPaloma()

    # key = MnemonicKey(
    #     mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    # )
    # test1 = paloma.wallet(key=key)
    test1 = paloma.wallets["test1"]

    msg = MsgSend(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnwcazay",
        Coins(ugrain=30000),
    )
    inputs = [
        MultiSendInput(
            address="paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
            coins=Coins(ugrain=30000),
        )
    ]
    outputs = [
        MultiSendOutput(
            address="paloma17lmam6zguazs5q5u6z5mmx76uj63gldnwcazay",
            coins=Coins(ugrain=10000),
        ),
        MultiSendOutput(
            address="paloma1av6ssz7k4xpc5nsjj2884nugakpp874ae0krx7",
            coins=Coins(ugrain=20000),
        ),
    ]
    msgMulti = MsgMultiSend(inputs, outputs)

    opt = CreateTxOptions(
        msgs=[msg, msgMulti], memo="send test", gas_adjustment=1.5, gas_prices="1ugrain"
    )
    # tx = test1.create_tx(opt)
    tx = test1.create_and_sign_tx(opt)
    print("SIGNED TX", tx)

    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
