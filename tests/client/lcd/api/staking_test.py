import re

from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.client.lcd.params import PaginationOptions
from paloma_sdk.key.mnemonic import MnemonicKey

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="pisco-1",
)

pagOpt = PaginationOptions(limit=1, count_total=True)

mk1 = MnemonicKey(
    mnemonic="nut praise glare false post crane clinic nothing happy effort loyal point parent few series task base maximum insect glass twice inflict tragic cancel"
)
mk2 = MnemonicKey(
    mnemonic="invite tape senior armor tragic punch actor then patrol mother version impact floor begin fitness tool street lava evidence lemon oval width soda actual"
)

test1_address = paloma.wallet(mk1).key.acc_address
test2_address = paloma.wallet(mk2).key.acc_address
validator1_address = "palomavaloper1thuj2a8sgtxr7z3gr39egng3syqqwas4hmvvlg"
validator2_address = "palomavaloper1q33jd4t8788ckkq8u935wtxstjnphcsdne3gud"


def test_delegations():

    result = paloma.staking.delegations(
        validator=validator1_address,
        delegator=None,
        params=pagOpt,
    )

    assert result is not None

    result = paloma.staking.delegations(
        validator=None,
        delegator=test1_address,
        params=pagOpt,
    )

    assert result is not None

    result = paloma.staking.delegations(
        validator=validator1_address,
        delegator=test1_address,
    )
    assert result is not None

    result = paloma.staking.delegation(
        validator=validator1_address,
        delegator=test1_address,
    )
    assert result is not None


# Blocked : unbond on testnet
# def test_unbonding():
#     result = paloma.staking.unbonding_delegations(
#         validator=validator1_address,
#         delegator=None
#     )
#     assert len(result[0]) >0

#     result = paloma.staking.unbonding_delegations(
#         validator=None,
#         delegator=test1_address,
#         params=pagOpt,
#     )
#     assert len(result[0]) >0

#     result = paloma.staking.unbonding_delegation(
#         validator=validator_address,
#         delegator=test1_address
#     )
#     assert result is not None


def test_validators():
    _pagOpt = PaginationOptions(limit=3, count_total=True, reverse=False)
    result = paloma.staking.validators(_pagOpt)
    assert result is not None
    result = paloma.staking.validator(validator1_address)
    assert result is not None


# Blocked : due to completion_time
# def test_redelagations():
#     _pagOpt = PaginationOptions(limit=1, count_total=True, reverse=False)
#     result = paloma.staking.redelegations(
#         test1_address, params=_pagOpt
#     )
#     assert result[0] is not None

#     result = paloma.staking.redelegations(
#         test1_address,
#         validator_src=validator1_address,
#         params=_pagOpt
#     )
#     assert(result[0] is not None)

#     result = paloma.staking.redelegations(
#         test1_address,
#         validator_dst=validator2_address,
#         params=_pagOpt
#     )
#     assert(result[0] is not None)

#     result = paloma.staking.redelegations(
#         test1_address,
#         validator_src=validator1_address,
#         validator_dst=validator2_address
#     )
#     assert(result is not None)

# def test_bonded_validators():
#     result = paloma.staking.bonded_validators(
#         test1_address, pagOpt
#     )
#     assert result is not None


def test_pool():
    result = paloma.staking.pool()
    assert result is not None


def test_parameters():
    result = paloma.staking.parameters()
    assert result.get("unbonding_time")
    assert result.get("max_validators")
    assert result.get("max_entries")
    assert result.get("historical_entries")
    assert result.get("bond_denom")
