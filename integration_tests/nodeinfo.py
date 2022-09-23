from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(
    chain_id="pisco-1",
    url="https://pisco-lcd.paloma.dev/",
)
res = paloma.tendermint.node_info()
print(res)
