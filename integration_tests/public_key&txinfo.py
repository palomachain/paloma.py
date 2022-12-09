import asyncio

import requests

from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.core import Coins
from paloma_sdk.core.public_key import SimplePublicKey, ValConsPubKey
from paloma_sdk.core.tx import TxInfo
from paloma_sdk.key.key import Key
from paloma_sdk.util import hash

light_clinet_address = "https://lcd.testnet.palomaswap.com"
chain_id = "pisco-1"
gas_prices = requests.get("https://pisco-fcd.paloma.dev/v1/txs/gas_prices").json()
paloma = AsyncLCDClient(
    chain_id=chain_id,
    url=light_clinet_address,
    gas_prices=Coins(ugrain=gas_prices["ugrain"]),
    gas_adjustment=1.2,
)


# Fix SimplePublicKey{from_data, to_data, from_amino, to_amino, from_proto, to_proto, address}
# Fix ValConsPubKey{from_data, to_data, from_amino, to_amino, from_proto, to_proto, address}
# Fix ModeInfoSingle{from_data, to_data}
# Fix JSONSerializable.to_data
# Fix TxInfo.to_data
# Fix TxLog{from_proto, to_proto}
# Fix TxBody.from_data
async def main():
    async with paloma:
        # Test `SimplePublicKey`
        simplePublicKey_og = SimplePublicKey.from_data(
            dict(key=b"A38NTjQrcD4p64693hRsYF4aEdFqhbA8pzRNj3NGO4P3")
        )
        data = simplePublicKey_og.to_data()
        simplePublicKey = SimplePublicKey.from_data(data)
        print(
            f"test: SimplePublicKey{{to_data, from_data}} {simplePublicKey_og == simplePublicKey}"
        )
        amino = simplePublicKey.to_amino()
        simplePublicKey = SimplePublicKey.from_amino(amino)
        print(
            f"test: SimplePublicKey{{to_amino, from_amino}} {simplePublicKey_og == simplePublicKey}"
        )
        proto = simplePublicKey.to_proto()
        simplePublicKey = SimplePublicKey.from_proto(proto)
        print(
            f"test: SimplePublicKey{{to_proto, from_proto}} {simplePublicKey_og == simplePublicKey}"
        )
        print(f"SimplePublicKey.address: {simplePublicKey.address()}")

        # Test compatibility with `Key`
        key = Key(simplePublicKey)
        print(
            f"test: SimplePublicKey.address == Key.acc_address {simplePublicKey.address() == key.acc_address}\n"
        )

        # Test `ValConsPubKey`
        val_pubkey_og = ValConsPubKey.from_data(key.public_key.to_data())
        data = val_pubkey_og.to_data()
        val_pubkey = ValConsPubKey.from_data(data)
        print(
            f"test: ValConsPubKey{{to_data, from_data}} {val_pubkey_og == val_pubkey}"
        )
        amino = val_pubkey_og.to_amino()
        val_pubkey = ValConsPubKey.from_amino(amino)
        print(
            f"test: ValConsPubKey{{to_amino, from_amino}} {val_pubkey_og == val_pubkey}"
        )
        proto = val_pubkey_og.to_proto()
        val_pubkey = ValConsPubKey.from_proto(proto)
        print(
            f"test: ValConsPubKey{{to_proto, from_proto}} {val_pubkey_og == val_pubkey}"
        )
        print(f"ValConsPubKey.address: {val_pubkey.address()}\n")

        # Test `AsyncTxAPI`{encode, decode, hash}
        bi = await paloma.tendermint.block_info(90000)
        # for encoded_tx in bi["block"]["data"]["txs"]:
        print(bi)
        encoded_tx = bi["block"]["data"]["txs"][0]
        txhash = hash.hash_amino(encoded_tx)
        # print(txhash)
        # print(encoded_tx)
        tx_from_proto = await paloma.tx.decode(encoded_tx)
        # print(decoded_tx)
        hash_from_proto = await paloma.tx.hash(tx_from_proto)
        # print(hash_from_proto)
        print(f"hash_from_proto==txhash {hash_from_proto == txhash}")
        if hash_from_proto != txhash:
            tx_info = await paloma.tx.tx_info(txhash)
            tx_from_data = tx_info.tx
            hash_from_data = await paloma.tx.hash(tx_from_data)
            print(f"hash_from_data==txhash {hash_from_data == txhash}")
            print(
                f"hash_from_data==hash_from_proto {hash_from_data == hash_from_proto}"
            )
            print(f"tx_from_proto==tx_from_data {tx_from_proto == tx_from_data}")
            if tx_from_proto != tx_from_data:
                print(tx_from_data)
                print(tx_from_proto)

        encoded_tx = await paloma.tx.encode(tx_from_proto)
        print(f"encoded_tx==encoded_tx {encoded_tx == encoded_tx}")
        # print(new_encoded_tx)
        decoded_tx = await paloma.tx.decode(encoded_tx)
        print(f"decoded_tx==tx_from_proto {decoded_tx == tx_from_proto}\n")

        # Test `Tx`, `TxLog` and `TxInfo`
        txhash_og = "3DAC0887F6ABD43C417B394A03B611104F313CC6B6C6A763A92FF8F184675D9B"
        tx_og = await paloma.tx.tx_info(txhash_og)
        data = tx_og.to_data()
        tx = TxInfo.from_data(data)
        print(f"test: Tx{{to_data, from_data}} {tx.tx == tx_og.tx}")
        print(f"test: TxBody{{to_data, from_data}} {tx.tx.body == tx_og.tx.body}")
        print(f"test: TxInfo{{to_data, from_data}} {tx == tx_og}")
        if tx != tx_og:
            print(tx)
            print(tx_og)
        proto = tx.to_proto()
        tx = TxInfo.from_proto(proto)
        print(f"test: Tx{{to_proto, from_proto}} {tx.tx == tx_og.tx}")
        print(f"test: TxLog{{to_proto, from_proto}} {tx.logs == tx_og.logs}")
        print(f"test: TxInfo{{to_proto, from_proto}} {tx == tx_og}")
        if tx != tx_og:
            print(tx)
            print(tx_og)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
