from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.client.lcd.params import PaginationOptions

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_tx_info():
    result = paloma.tx.tx_info(
        "903B567F551D7D8DDE5146C907B3590843A0DEAEEAFA0CEC93CEA8378DE11123"
    )

    assert result is not None
    assert (
        result.txhash
        == "903B567F551D7D8DDE5146C907B3590843A0DEAEEAFA0CEC93CEA8378DE11123"
    )


def test_search():
    result = paloma.tx.search(
        [
            ("tx.height", 920183),
            ("message.sender", "paloma1cyyzpxplxdzkeea7kwsydadg87357qna8rgwj8"),
        ]
    )

    assert len(result["txs"]) > 0
    assert (
        result["txs"][0].txhash
        == "903B567F551D7D8DDE5146C907B3590843A0DEAEEAFA0CEC93CEA8378DE11123"
    )


# def test_tx_infos_by_height():
#     result = paloma.tx.tx_infos_by_height()
#     assert result is not None


def test_tx_infos_by_height_with_height():
    result = paloma.tx.tx_infos_by_height(1)
    assert result is not None
