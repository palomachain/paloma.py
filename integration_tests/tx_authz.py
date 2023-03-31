from paloma_sdk.client.lcd.api.tx import CreateTxOptions
from paloma_sdk.client.localpaloma import LocalPaloma
from paloma_sdk.core.authz import (
    MsgExecAuthorized,
    MsgGrantAuthorization,
    MsgRevokeAuthorization,
)


def main():
    paloma = LocalPaloma()
    test1 = paloma.wallets["test1"]

    msgG = MsgGrantAuthorization(
        granter="paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td5wpjhf",
        grantee="paloma17lmam6zguazs5q5u6z5mmx76uj63gldnwcazay"
        """
        grant=Grant(
            authorization=...,
            expiration=
        )
        """,
    )
    msgE = MsgExecAuthorized()
    msgR = MsgRevokeAuthorization()

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgG]))
    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgE]))
    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")

    tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[msgR]))
    result = paloma.tx.broadcast(tx)
    print(f"RESULT:{result}")


main()
