from ._base import BaseAsyncAPI, sync_bind
from ..wallet import Wallet
from .tx import Tx, CreateTxOptions, SignerOptions
from paloma_sdk.core.wasm import MsgInstantiateContract
from paloma_sdk.core.coins import Coins

__all__ = ["AsyncCw20API", "Cw20API"]


class AsyncCw20API(BaseAsyncAPI):
    async def deploy(self, wallet: Wallet, code_id: int, name: str, symbol: str, decimals: int, total_supply: int) -> Tx:
        """Deploy the Cw20 smart contract using code id.
        """
        instantiate_msg = {"name": name, "symbol": symbol, "decimals": decimals, "initial_balances": [{"address": wallet.key.acc_address, "amount": total_supply}]}
        funds = Coins.from_str("0ugrain")
        tx = wallet.create_and_sign_tx(CreateTxOptions(msgs=[MsgInstantiateContract(wallet.key.acc_address, None, code_id, "CW20", instantiate_msg, funds)]))
        return tx


class Cw20API(AsyncCw20API):
    @sync_bind(AsyncCw20API.deploy)
    def deploy(self, code_id, name, symbol, decimals, total_supply) -> Tx:
        pass

    deploy.__doc__ = AsyncCw20API.deploy.__doc__
