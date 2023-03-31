from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.client.localpaloma import LocalPaloma
from paloma_sdk.core import Coin, Coins
from paloma_sdk.core.distribution import (MsgFundCommunityPool,
                                          MsgSetWithdrawAddress,
                                          MsgWithdrawDelegatorReward,
                                          MsgWithdrawValidatorCommission)


def main():
    paloma = LocalPaloma()
    test1 = paloma.wallets["test1"]
    validator = paloma.wallets["validator"]

    msgFund = MsgFundCommunityPool(
        depositor="paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        amount=Coins("1000000ugrain"),
    )
    msgSet = MsgSetWithdrawAddress(
        delegator_address="paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        withdraw_address="paloma1av6ssz7k4xpc5nsjj2884nugakpp874ae0krx7",
    )
    msgWCom = MsgWithdrawValidatorCommission(
        validator_address="palomavaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5"
    )
    msgWDel = MsgWithdrawDelegatorReward(
        delegator_address="paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        validator_address="palomavaloper1dcegyrekltswvyy0xy69ydgxn9x8x32zdy3ua5",
    )

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgFund]))
    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgSet]))
    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgWDel]))
    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = validator.create_and_sign_tx(CreateTxOptions(msgs=[msgWCom]))
    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
