from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.client.lcd.params import PaginationOptions

paloma = LCDClient(
    url="https://pisco-lcd.paloma.dev/",
    chain_id="pisco-1",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_balance():
    result, _ = paloma.bank.balance(
        address="paloma1rk6tvacasnnyssfnn00zl7wz43pjnpn7vayqv6"
    )
    assert result.to_data()
    assert result.get("uluna").amount > 0


def test_balance_with_pagination():
    result, _ = paloma.bank.balance(
        address="paloma1rk6tvacasnnyssfnn00zl7wz43pjnpn7vayqv6", params=pagOpt
    )

    assert result.to_data()
    assert result.get("uluna").amount > 0


def test_total():
    result, _ = paloma.bank.total()

    assert result.to_data()


def test_total_with_pagination():
    result, _ = paloma.bank.total(pagOpt)

    assert result.to_data()


def test_spendable_balances():
    result, _ = paloma.bank.spendable_balances(
        address="paloma1rk6tvacasnnyssfnn00zl7wz43pjnpn7vayqv6"
    )

    assert result.to_data()
