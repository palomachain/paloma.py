from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.client.lcd.params import PaginationOptions

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="pisco-1",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_tx_info():
    result = paloma.tx.tx_info(
        "10C4732BAE613ACCEF490D19B8B9647EC3D26B6E8F1AB1277201035FE86552A4"
    )

    assert result is not None
    assert (
        result.txhash
        == "10C4732BAE613ACCEF490D19B8B9647EC3D26B6E8F1AB1277201035FE86552A4"
    )


def test_search():
    result = paloma.tx.search(
        [
            ("tx.height", 42508),
            ("message.sender", "paloma1h8ljdmae7lx05kjj79c9ekscwsyjd3yr8wyvdn"),
        ]
    )

    assert len(result["txs"]) > 0
    assert (
        result["txs"][0].txhash
        == "10C4732BAE613ACCEF490D19B8B9647EC3D26B6E8F1AB1277201035FE86552A4"
    )


def test_tx_infos_by_height():
    result = paloma.tx.tx_infos_by_height()
    assert result is not None


def test_tx_infos_by_height_with_height():
    result = paloma.tx.tx_infos_by_height(1)
    assert result is not None
