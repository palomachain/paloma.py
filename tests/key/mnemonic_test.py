import base64

from paloma_sdk.client.lcd.api.tx import CreateTxOptions, SignerOptions
from paloma_sdk.client.lcd.lcdclient import LCDClient
from paloma_sdk.core import Coins, SignDoc
from paloma_sdk.core.bank import MsgSend
from paloma_sdk.core.fee import Fee
from paloma_sdk.key.mnemonic import MnemonicKey


def test_derivation():
    mk = MnemonicKey(
        "wonder caution square unveil april art add hover spend smile proud admit modify old copper throw crew happy nature luggage reopen exhibit ordinary napkin"
    )
    assert mk.acc_address == "paloma1ml03954f5xvm2lftuqwp2mtf7zs2c9w66ucmz4"
    assert (
        mk.acc_pubkey
        == "palomapub1addwnpepqvlwduqg2l8gzg0uuemsu4nrsufaydeackm59kkljyp3vnpzhyv6y6fg4y9"
    )
    assert mk.val_address == "palomavaloper1ml03954f5xvm2lftuqwp2mtf7zs2c9w64v085x"
    assert (
        mk.val_pubkey
        == "palomavaloperpub1addwnpepqvlwduqg2l8gzg0uuemsu4nrsufaydeackm59kkljyp3vnpzhyv6ye8jwy3"
    )


def test_random():
    mk1 = MnemonicKey()
    mk2 = MnemonicKey()
    assert mk1.mnemonic != mk2.mnemonic


def test_signature():

    paloma = LCDClient(
        url="https://lcd.testnet.palomaswap.com", chain_id="paloma-testnet-15"
    )

    mk = MnemonicKey(
        "island relax shop such yellow opinion find know caught erode blue dolphin behind coach tattoo light focus snake common size analyst imitate employ walnut"
    )

    account = paloma.wallet(mk)

    send = MsgSend(
        mk.acc_address,
        "paloma1wg2mlrxdmnnkkykgqg4znky86nyrtc457sxe5f",
        dict(ugrain="100000000"),
    )

    tx = paloma.tx.create(
        signers=[
            SignerOptions(
                address=mk.acc_address, sequence=0, public_key=account.key.public_key
            )
        ],
        options=CreateTxOptions(
            msgs=[send], memo="memo", fee=Fee(200000, Coins.from_str("100000ugrain"))
        ),
    )

    signDoc = SignDoc(
        chain_id=paloma.chain_id,
        account_number=1234,
        sequence=0,
        auth_info=tx.auth_info,
        tx_body=tx.body,
    )

    signature = account.key.create_signature(signDoc)
    sigBytes = base64.b64encode(signature.data.single.signature)
    assert (
        sigBytes
        == b"cS2EmpEmii+RUS40aI8v2NACVM41gewA8sq1e+y4J8c6gduDdcMCA78RB2vUXopBKOpq/VHAvEiTIgV+Q6b/TQ=="
    )

    signature_amino = account.key.create_signature_amino(signDoc)
    sigBytes2 = base64.b64encode(signature_amino.data.single.signature)
    assert (
        sigBytes2
        == b"GNeQX0eRFa+4ylP2ArBFVn7h9pommOZEd2z4fC7idzVHg0qBBRV2pAa2AXP9AU5Wc9ydrx7lk62YRvHVIBQSXw=="
    )
