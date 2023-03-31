from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.client.lcd.params import PaginationOptions

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_balance():
    result, _ = paloma.bank.balance(
        address="paloma17esj9dnjhnpezfqmpwdwg2yldnc3udrdv5e76w"
    )
    assert result.to_data()
    assert result.get("ugrain").amount > 0


def test_balance_with_pagination():
    result, _ = paloma.bank.balance(
        address="paloma17esj9dnjhnpezfqmpwdwg2yldnc3udrdv5e76w", params=pagOpt
    )

    assert result.to_data()
    assert result.get("ugrain").amount > 0


def test_total():
    result, _ = paloma.bank.total()

    assert result.to_data()


def test_total_with_pagination():
    result, _ = paloma.bank.total(pagOpt)

    assert result.to_data()


def test_spendable_balances():
    result, _ = paloma.bank.spendable_balances(
        address="paloma17esj9dnjhnpezfqmpwdwg2yldnc3udrdv5e76w"
    )

    assert result.to_data()
