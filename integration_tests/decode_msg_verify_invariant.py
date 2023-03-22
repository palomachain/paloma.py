from paloma_sdk.client.lcd import LCDClient


def main():
    paloma = LCDClient(
        url="https://lcd.testnet.palomaswap.com",
        chain_id="paloma-testnet-15",
    )

    print(paloma.tx.tx_infos_by_height(8152638))
    print(paloma.tx.tx_infos_by_height(8153558))


main()
