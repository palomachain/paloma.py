from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.core.bech32 import is_acc_address

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="pisco-1",
)


def test_rewards():
    result = paloma.distribution.rewards("paloma1mzhc9gvfyh9swxed7eaxn2d6zzc3msgftk4w9e")
    assert result.total.to_data()


def test_validator_commission():
    result = paloma.distribution.validator_commission(
        "palomavaloper1thuj2a8sgtxr7z3gr39egng3syqqwas4hmvvlg"
    )
    assert result.to_data()


def test_withdraw_address():
    result = paloma.distribution.withdraw_address(
        "paloma1mzhc9gvfyh9swxed7eaxn2d6zzc3msgftk4w9e"
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
