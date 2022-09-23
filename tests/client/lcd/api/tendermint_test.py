from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(
    url="https://pisco-lcd.paloma.dev/",
    chain_id="pisco-1",
)


def test_validator_set():
    result = paloma.tendermint.validator_set()
    print(result)


def test_validator_set_with_height():
    result = paloma.tendermint.validator_set(1)

    assert (
        result["validators"][0]["address"]
        == "palomavalcons15m2dkstenqhjefq4c95jrug402v27tug3ymwwv"
    )


def test_node_info():
    result = paloma.tendermint.node_info()

    assert result["default_node_info"]["network"] == "pisco-1"


def test_block_info():
    result = paloma.tendermint.block_info()
    print(result["block"]["header"]["height"])


def test_block_info_with_height():
    result = paloma.tendermint.block_info(1)
    print(result)


def test_syncing():
    result = paloma.tendermint.syncing()
    print(result)
