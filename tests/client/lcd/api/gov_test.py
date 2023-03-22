from paloma_sdk.client.lcd import LCDClient, PaginationOptions
from paloma_sdk.exceptions import LCDResponseError

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


pagOpt = PaginationOptions(limit=2, count_total=True)


def test_proposals():
    result = paloma.gov.proposals()
    assert result is not None


def test_proposals_with_pagination():
    result = paloma.gov.proposals(PaginationOptions(limit=2))
    assert result is not None


# Add proper proposal id for test
# def test_proposal():
#     result = paloma.gov.proposal(3)
#     assert result is not None


# # public lcd requires tx.height
# def test_proposer():
#     result = paloma.gov.proposer(3)
#     assert(result is not None)


# # public lcd requires tx.height
# def test_deposits():
#    result = paloma.gov.deposits(3)
#    assert(result is not None)


# # public lcd requires tx.height
# def test_deposits_with_pagination():
#     result = paloma.gov.deposits(3, params=pagOpt)
#     assert(result is not None)


# # public lcd requires tx.height
# def test_votes():
#     result = paloma.gov.votes(3)
#     assert(result is not None)


# # public lcd requires tx.height
# def test_votes_with_pagination():
#     result = paloma.gov.votes(3, pagOpt)
#     assert(result is not None)


# def test_tally():
#     result = paloma.gov.tally(3)
#     assert result is not None


def test_deposit_parameters():
    result = paloma.gov.deposit_parameters()
    assert result.get("min_deposit")
    assert result.get("max_deposit_period")


def test_voting_parameters():
    result = paloma.gov.voting_parameters()
    assert result.get("voting_period")


def test_tally_parameters():
    result = paloma.gov.tally_parameters()
    assert result.get("quorum")
    assert result.get("threshold")
    assert result.get("veto_threshold")


def test_parameters():
    result = paloma.gov.parameters()
    assert result.get("deposit_params")
    assert result.get("voting_params")
    assert result.get("tally_params")
