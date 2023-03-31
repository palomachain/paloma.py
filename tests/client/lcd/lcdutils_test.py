from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


def test_validators_with_voting_power():
    ### TODO endpoint is not defined "/validators?height="
    ### E               paloma_sdk.exceptions.LCDResponseError: Status 501 - {'code': 12, 'message': 'Not Implemented', 'details': []}

    # validators_with_voting_power = paloma.utils.validators_with_voting_power()
    # print(validators_with_voting_power)
    # assert validators_with_voting_power is not None
    
    pass
