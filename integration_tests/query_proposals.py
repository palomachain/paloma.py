from paloma_sdk.client.lcd import LCDClient, PaginationOptions
from paloma_sdk.client.lcd.api.gov import ProposalStatus

paloma = LCDClient(
    url="https://pisco-lcd.paloma.dev/",
    chain_id="pisco-1",
)


result, pagination = paloma.gov.proposals()

while pagination["next_key"] is not None:
    pagOpt = PaginationOptions(key=pagination["next_key"])
    result, pagination = paloma.gov.proposals(params=pagOpt)
    pagOpt.key = pagination["next_key"]
    print(result)


result, pagination = paloma.gov.proposals(
    options={
        "proposal_status": ProposalStatus.PROPOSAL_STATUS_DEPOSIT_PERIOD,
        "depositor": "paloma1w8wc2ke09242v7vjqd5frzw6ulpz4l7yrcwppt",
    }
)
print(result)
