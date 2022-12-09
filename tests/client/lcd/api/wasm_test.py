import pytest
from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.exceptions import LCDResponseError

paloma = LCDClient(
    url= "https://lcd.testnet.palomaswap.com/",
    chain_id="pisco-1",
)


def test_contract_info():
    result = paloma.wasm.contract_info(
        "paloma19xa33fjdjlz9qkafrw8qnrzrawc8h0vhxvfdhh6yk3f5qxuh2fps9e49zt"
    )
    assert result is not None


def test_code_info():
    result = paloma.wasm.code_info(72)

    assert result["code_id"] == 72
    assert result["creator"] == "paloma1mzhc9gvfyh9swxed7eaxn2d6zzc3msgftk4w9e"
    assert (
        result["data_hash"]
        == "CD686878A33E62CBCDAF7620E776096E4D15856CC03B0F12EDE66A1D5699D39D"
    )

def test_code_info_with_params():
    with pytest.raises(LCDResponseError):
        paloma.wasm.code_info(72, {"height": 100})
    
def test_contract_query():
    result = paloma.wasm.contract_query(
        "paloma19xa33fjdjlz9qkafrw8qnrzrawc8h0vhxvfdhh6yk3f5qxuh2fps9e49zt",
        {"get_count": {}},
    )
    assert result is not None

def test_contract_query_with_params():
    result = paloma.wasm.contract_query(
        "paloma19xa33fjdjlz9qkafrw8qnrzrawc8h0vhxvfdhh6yk3f5qxuh2fps9e49zt",
        {"get_count": {}},
        {"height": 	61027}
    )
    assert result == {'count':0}

    result = paloma.wasm.contract_query(
        "paloma19xa33fjdjlz9qkafrw8qnrzrawc8h0vhxvfdhh6yk3f5qxuh2fps9e49zt",
        {"get_count": {}},
        {"height": 	61028}
    )
    assert result == {'count':1}

def test_pinned_codes():
    result = paloma.wasm.pinned_codes()
    assert result["code_ids"] is not None
