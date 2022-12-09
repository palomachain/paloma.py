from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(chain_id="pisco-1", url="https://lcd.testnet.palomaswap.com")

res = paloma.auth.account_info(address="paloma1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v")
print(res)

res = paloma.auth.account_info(address="paloma1vk20anceu6h9s00d27pjlvslz3avetkvnph7p8")
print(res)
