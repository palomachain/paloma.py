from paloma_sdk.client.lcd import LCDClient, PaginationOptions
from paloma_sdk.core import Coins

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


def test_account_info():
    # base_account
    result = paloma.auth.account_info("paloma14c64c9wdmnz9n8e9uyvtg70755zn377eyf0s4x")

    assert result.address == "paloma14c64c9wdmnz9n8e9uyvtg70755zn377eyf0s4x"
    assert result.account_number == 0

    # delayed_vesting_account
    result = paloma.auth.account_info("paloma1t8mw9mlt28ax6qj88ra89fcv60n8uu7yfqus3r")

    assert (
        result.base_vesting_account.base_account.address
        == "paloma1t8mw9mlt28ax6qj88ra89fcv60n8uu7yfqus3r"
    )

    # continuous_vesting_account
    result = paloma.auth.account_info("paloma186wj7gy9q5syg0kls4cctgn23d9xh3d6h3dqq9")

    assert (
        result.base_vesting_account.base_account.address
        == "paloma186wj7gy9q5syg0kls4cctgn23d9xh3d6h3dqq9"
    )
    assert result.start_time == "1653300000"

    # periodic_vesting_account
    result = paloma.auth.account_info("paloma1auswfkggetjrhe8jxkzngfd26hugz55d64p0z6")

    assert (
        result.base_vesting_account.base_account.address
        == "paloma1auswfkggetjrhe8jxkzngfd26hugz55d64p0z6"
    )
    assert result.start_time == "1660000000"
    assert result.vesting_periods[0].length == 604800
    assert result.vesting_periods[0].amount == Coins("1000000000ugrain")
