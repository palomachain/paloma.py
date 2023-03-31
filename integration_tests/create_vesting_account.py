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
from paloma_sdk.client.lcd.api.tx import CreateTxOptions, SignerOptions
# import lcd_tx
from paloma_sdk.client.localpaloma import LocalPaloma
from paloma_sdk.core import Coin, Coins
from paloma_sdk.core.auth import (MsgCreatePeriodicVestingAccount,
                                  MsgCreateVestingAccount,
                                  MsgDonateAllVestingTokens, Period)
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.core.tx import SignMode
from paloma_sdk.key.key import SignOptions
from paloma_sdk.key.mnemonic import MnemonicKey


def main():
    paloma = LocalPaloma()

    seed = "notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    seed_pv = "father submit repeat detail wild blast wool cat machine sphere cute tool speak slogan double common camp lab example subject winter better grit property"
    seed_v = "very police soap exchange club analyst identify injury skate sibling dash trust gauge assault work way business sniff orient female bring truth exit adult"
    key = MnemonicKey(mnemonic=seed)
    key_pv = MnemonicKey(mnemonic=seed_pv)
    key_v = MnemonicKey(mnemonic=seed_v)

    wallet = paloma.wallet(key)
    wallet_pv = paloma.wallet(key_pv)
    wallet_v = paloma.wallet(key_v)
    print(key_pv.acc_address)
    print(key_v.acc_address)
    cva = MsgCreateVestingAccount(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        key_v.acc_address,
        Coins("2000ugrain"),
        1659130372,
        False,
    )

    cpva = MsgCreatePeriodicVestingAccount(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        key_pv.acc_address,
        1659130372,
        [Period(100, Coins("1000ugrain"))],
    )

    tx = wallet.create_and_sign_tx(
        CreateTxOptions(
            msgs=[cva, cpva],
        )
    )
    result = paloma.tx.broadcast(tx)

    send1 = MsgSend(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        key_v.acc_address,
        Coins("100000ugrain"),
    )
    send2 = MsgSend(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        key_pv.acc_address,
        Coins("100000ugrain"),
    )

    tx = wallet.create_and_sign_tx(
        CreateTxOptions(msgs=[send1, send2], memo="test from paloma.py")
    )
    result = paloma.tx.broadcast(tx)

    print("send to vesting and periodic vesting account : ", result)

    tx = wallet_v.create_and_sign_tx(
        CreateTxOptions(msgs=[MsgDonateAllVestingTokens(key_v.acc_address)])
    )
    result = paloma.tx.broadcast(tx)

    print("donate all tokens in vesting account : ", result)
    tx = wallet_pv.create_and_sign_tx(
        CreateTxOptions(msgs=[MsgDonateAllVestingTokens(key_pv.acc_address)])
    )
    result = paloma.tx.broadcast(tx)
    print("donate all tokens in periodic vesting account : ", result)


main()
