from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="pisco-1",
)


def test_validators_with_voting_power():
    validators_with_voting_power = paloma.utils.validators_with_voting_power()
    print(validators_with_voting_power)
    assert validators_with_voting_power is not None
