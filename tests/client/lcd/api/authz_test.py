from paloma_sdk.client.lcd import LCDClient, PaginationOptions

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


def test_grants():
    result = paloma.authz.grants(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    )
    assert len(result) == 0

    result = paloma.authz.granter("paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")
    assert len(result) == 0

    result = paloma.authz.grantee("paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")

    assert len(result) == 0
