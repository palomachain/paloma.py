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
    assert mk.acc_address == "paloma1jnzv225hwl3uxc5wtnlgr8mwy6nlt0vztv3qqm"
    assert (
        mk.acc_pubkey
        == "palomapub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5nwzrf9"
    )
    assert mk.val_address == "palomavaloper1jnzv225hwl3uxc5wtnlgr8mwy6nlt0vztraasg"
    assert (
        mk.val_pubkey
        == "palomavaloperpub1addwnpepqt8ha594svjn3nvfk4ggfn5n8xd3sm3cz6ztxyugwcuqzsuuhhfq5y7accr"
    )


def test_random():
    mk1 = MnemonicKey()
    mk2 = MnemonicKey()
    assert mk1.mnemonic != mk2.mnemonic


def test_signature():

    paloma = LCDClient(url="https://lcd.testnet.palomaswap.com", chain_id="pisco-1")

    mk = MnemonicKey(
        "island relax shop such yellow opinion find know caught erode blue dolphin behind coach tattoo light focus snake common size analyst imitate employ walnut"
    )

    account = paloma.wallet(mk)

    send = MsgSend(
        mk.acc_address,
        "paloma1wg2mlrxdmnnkkykgqg4znky86nyrtc45q336yv",
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
        == b"3zTLdy+PLc0CFPyVt4idBTQ/gwYLJ4G5z+R+tTHRz8lMy3oYwGWv+tZbxIJDfrAgpEM+YO8sO5LsjYmH5khpOQ=="
    )

    signature_amino = account.key.create_signature_amino(signDoc)
    sigBytes2 = base64.b64encode(signature_amino.data.single.signature)
    assert (
        sigBytes2
        == b"4Udg3FbCLAVd5vxrI5EY5Dv6A9DXKarRzD8bamE36qsH1JoelXbmf1pg0GRG4CkxySfAlDfHdCsK8FOGv9fCNA=="
    )
