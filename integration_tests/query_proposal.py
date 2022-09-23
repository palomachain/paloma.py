from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(chain_id="pisco-1", url="https://pisco-lcd.paloma.dev")
res = paloma.gov.deposits(proposal_id=5333)
print(res)
res = paloma.gov.votes(proposal_id=5333)
print(res)
