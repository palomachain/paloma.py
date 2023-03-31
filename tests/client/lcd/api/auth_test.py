from paloma_sdk.client.lcd import LCDClient, PaginationOptions
from paloma_sdk.core import Coins

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


def test_account_info():
    # base_account
    result = paloma.auth.account_info("paloma18d4cfq63h4a9cz49d86pr84hpang7yvqq9ucwf")

    assert result.address == "paloma18d4cfq63h4a9cz49d86pr84hpang7yvqq9ucwf"
    assert result.account_number == 0
