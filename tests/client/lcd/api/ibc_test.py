from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="pisco-1",
)


def test_parameters():
    result = paloma.ibc.parameters()
    assert result.get("allowed_clients")
