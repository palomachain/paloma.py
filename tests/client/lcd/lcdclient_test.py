import asynctest
from aioresponses import aioresponses

from paloma_sdk.client.lcd import AsyncLCDClient, LCDClient

"""
class TestDoSessionGet(asynctest.TestCase):
    @aioresponses()
    def test_makes_request_to_expected_url(self, mocked):
        mocked.get(
            "https://lcd.testnet.palomaswap.com/cosmos/base/tendermint/v1beta1/node_info",
            status=200,
            body='{"response": "test"}',
        )
        paloma = LCDClient(chain_id="pisco-1", url="https://lcd.testnet.palomaswap.com/")

        resp = paloma.tendermint.node_info()
        assert resp == {"response": "test"}
        paloma.session.close()

    @aioresponses()
    async def test_makes_request_to_expected_url_async(self, mocked):
        mocked.get(
            "https://lcd.testnet.palomaswap.com/cosmos/base/tendermint/v1beta1/node_info",
            status=200,
            body='{"response": "test"}',
        )
        paloma = AsyncLCDClient(chain_id="pisco-1", url="https://lcd.testnet.palomaswap.com/")

        resp = await paloma.tendermint.node_info()
        print(resp)
        assert resp == {"response": "test"}
        paloma.session.close()


if __name__ == "__main__":
    asynctest.main()
"""
