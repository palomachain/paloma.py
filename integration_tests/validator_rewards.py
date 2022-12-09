from paloma_sdk.client.lcd import LCDClient

paloma = LCDClient(chain_id="pisco-1", url="https://lcd.testnet.palomaswap.com")
print(
    paloma.distribution.validator_rewards(
        "palomavaloper1259cmu5zyklsdkmgstxhwqpe0utfe5hhyty0at"
    )
)
