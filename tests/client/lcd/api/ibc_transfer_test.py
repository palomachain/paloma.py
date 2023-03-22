from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


def test_parameters():
    result = paloma.ibc_transfer.parameters()
    assert result.get("send_enabled")
    assert result.get("receive_enabled")
