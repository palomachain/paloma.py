from paloma_sdk.client.lcd import LCDClient
from paloma_sdk.util.contract import get_contract_events

tequila = LCDClient(url="https://lcd.testnet.palomaswap.com", chain_id="pisco-1")
tx_info = tequila.tx.tx_info(
    "D1E80F27435215FF097141C804EDE51C87718355CA8A6A397CC2346144F19D04"
)
print(get_contract_events(tx_info))
