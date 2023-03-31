from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.core.bech32 import is_acc_address

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


def test_rewards():
    result = paloma.distribution.rewards(
        "paloma15gvyk43x406v7kcd4rff5qfutqmcnpj3p4ea9g"
    )
    assert result.total.to_data()


def test_validator_commission():
    result = paloma.distribution.validator_commission(
        "palomavaloper15gvyk43x406v7kcd4rff5qfutqmcnpj3w9wpnm"
    )
    assert result.to_data()


def test_withdraw_address():
    result = paloma.distribution.withdraw_address(
        "paloma15gvyk43x406v7kcd4rff5qfutqmcnpj3p4ea9g"
    )
    assert is_acc_address(result)


def test_comminity_pool():
    result = paloma.distribution.community_pool()
    assert result.to_data()


def test_parameters():
    result = paloma.distribution.parameters()
    assert result.get("community_tax")
    assert result.get("base_proposer_reward")
    assert result.get("bonus_proposer_reward")
    assert result.get("withdraw_addr_enabled")
