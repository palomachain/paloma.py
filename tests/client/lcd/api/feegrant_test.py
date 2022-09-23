from paloma_sdk.client.lcd import LCDClient, PaginationOptions

paloma = LCDClient(
    url="https://pisco-lcd.paloma.dev/",
    chain_id="pisco-1",
)


pagOpt = PaginationOptions(limit=2, count_total=True)


def test_allowances():
    result, _ = paloma.feegrant.allowances(
        "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp"
    )
    assert result is not None
    assert len(result) >= 0


def test_allowance():
    result = paloma.feegrant.allowance(
        "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    )

    assert result is not None
    assert result["granter"] == "paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v"
    assert result["grantee"] == "paloma17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp"
