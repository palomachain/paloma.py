from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(
    chain_id="pisco-1",
    url="https://lcd.testnet.palomaswap.com/",
)
res = paloma.tendermint.node_info()
print(res)
