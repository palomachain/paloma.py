from typing import Optional

from ..params import APIParams
from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncTendermintAPI", "TendermintAPI"]


class AsyncTendermintAPI(BaseAsyncAPI):
    async def node_info(self, params: Optional[APIParams] = None) -> dict:
        """Fetches the curent connected node's information.

        Args:
            params (APIParams): optional parameters

        Returns:
            dict: node information
        """
        return await self._c._get("/status", params)
        # return {
        #     "default_node_info": res["default_node_info"],
        #     "application_version": res["application_version" ""],
        # }

    async def syncing(self, params: Optional[APIParams] = None) -> bool:
        """Fetches whether the curent connect node is syncing with the network.

        Args:
            params (APIParams): optional parameters

        Returns:
            bool: syncing status
        """
        return await self._c._get("/status", params)

    async def validator_set(
        self, height: Optional[int] = None, params: Optional[APIParams] = None
    ) -> dict:
        """Fetches the validator set for a height. If no height is given, defaults to latest.

        Args:
            height (int, optional): block height.
            params (APIParams): optional parameters

        Returns:
            dict: validator set
        """
        x = "" if height is None else height
        return await self._c._get(f"/validators?height={x}", params)

    async def block_info(
        self, height: Optional[int] = None, params: Optional[APIParams] = None
    ) -> dict:
        """Fetches the block information for a given height. If no height is given, defaults to latest block.

        Args:
            height (int, optional): block height.
            params (APIParams): optional parameters

        Returns:
            dict: block info
        """
        x = "" if height is None else height
        return await self._c._get(f"/block?height={x}", params)


class TendermintAPI(AsyncTendermintAPI):
    @sync_bind(AsyncTendermintAPI.node_info)
    def node_info(self, params: Optional[APIParams] = None) -> dict:
        pass

    node_info.__doc__ = AsyncTendermintAPI.node_info.__doc__

    @sync_bind(AsyncTendermintAPI.syncing)
    def syncing(self, params: Optional[APIParams] = None) -> bool:
        pass

    syncing.__doc__ = AsyncTendermintAPI.syncing.__doc__

    @sync_bind(AsyncTendermintAPI.validator_set)
    def validator_set(
        self, height: Optional[int] = None, params: Optional[APIParams] = None
    ) -> dict:
        pass

    validator_set.__doc__ = AsyncTendermintAPI.validator_set.__doc__

    @sync_bind(AsyncTendermintAPI.block_info)
    def block_info(
        self, height: Optional[int] = None, params: Optional[APIParams] = None
    ) -> dict:
        pass

    block_info.__doc__ = AsyncTendermintAPI.block_info.__doc__
