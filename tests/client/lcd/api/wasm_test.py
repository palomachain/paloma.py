import pytest

from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.exceptions import LCDResponseError

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


def test_contract_info():
    result = paloma.wasm.contract_info(
        "paloma1447waysnqg3w67j52kmjca6gpp4jw7cjpyxt9mkuw2lkc0s8624qvvw72t"
    )
    assert result is not None


def test_code_info():
    result = paloma.wasm.code_info(32)

    assert result["code_id"] == 32
    assert result["creator"] == "paloma1cyyzpxplxdzkeea7kwsydadg87357qna8rgwj8"
    assert (
        result["data_hash"]
        == "9DF34695F28BE06F9C0D9D61DB6DC0035E5A61937FE13325DF58ADCF85020A5F"
    )


def test_code_info_with_params():
    # with pytest.raises(LCDResponseError):
    paloma.wasm.code_info(32, {"height": 1})


def test_contract_query():
    result = paloma.wasm.contract_query(
        "paloma19usnw37lvx8jm6wehqqk56lxxcjd807py5l3trhrv92zy2s7rxsqdp6gee",
        {"token_info": {}},
    )
    print(result)
    assert result is not None


def test_contract_query_with_params():
    result = paloma.wasm.contract_query(
        "paloma19usnw37lvx8jm6wehqqk56lxxcjd807py5l3trhrv92zy2s7rxsqdp6gee",
        {"balance": {"address": "paloma1cyyzpxplxdzkeea7kwsydadg87357qna8rgwj8"}},
    )
    assert result == {"balance": "999998000000000"}


def test_pinned_codes():
    result = paloma.wasm.pinned_codes()
    assert result["code_ids"] is not None
