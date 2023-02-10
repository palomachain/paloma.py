import json
import base64
from pathlib import Path
from typing import Optional

from ._base import BaseAsyncAPI, sync_bind
from ..wallet import Wallet
from .tx import CreateTxOptions
from terra_proto.cosmwasm.wasm.v1 import AccessType
from paloma_sdk.core.wasm.data import AccessConfig
from paloma_sdk.core.wasm import MsgInstantiateContract, MsgExecuteContract, MsgStoreCode
from paloma_sdk.core.scheduler import MsgCreateJob
from paloma_sdk.core.coins import Coins
from paloma_sdk.core.broadcast import BlockTxBroadcastResult
from paloma_sdk.util.contract import read_file_as_b64

__all__ = ["AsyncJobSchedulerAPI", "JobSchedulerAPI"]


class AsyncJobSchedulerAPI(BaseAsyncAPI):
    async def create_job(
        self,
        wallet: Wallet,
        job_id: str,
        contract_address: str,
        abi: dict,
        payload: str,
        chain_type: str,
        chain_reference_id: str
    ) -> BlockTxBroadcastResult:
        """create job
        """
        definition = {"abi": json.dumps(abi).replace('"', '\\"'), "address": contract_address}
        definition_bytes = json.dumps(definition).encode("ascii")
        definition_base64 = base64.b64encode(definition_bytes).decode("ascii")
        payload_bytes = json.dumps({"hexPayload": payload}).encode("ascii")
        payload_base64 = base64.b64encode(payload_bytes).decode("ascii")
        create_tx = await wallet.create_and_sign_tx(
            CreateTxOptions(
                msgs=[
                    MsgCreateJob(wallet.key.acc_address, {
                        "ID": job_id,
                        "owner": "",
                        "routing": {
                            "chainType": chain_type,
                            "chainReferenceID": chain_reference_id
                        },
                        "definition": definition_base64,
                        "payload": payload_base64,
                        "isPayloadModifiable": True,
                        "permissions": {
                            "whitelist": [],
                            "blacklist": []
                        },
                        "triggers": [],
                        "address": ""
                    })
                ],
                gas="10000"
            )
        )
        create_tx_result = await self._c.tx.broadcast(create_tx)
        return create_tx_result

    async def execute_job(
        self,
        wallet: Wallet,
        job_id: str,
        contract_address: str,
        abi: dict,
        payload: str,
        chain_type: str,
        chain_reference_id: str
    ) -> BlockTxBroadcastResult:
        """execute job
        """
        definition = {"abi": json.dumps(abi).replace('"', '\\"'), "address": contract_address}
        definition_bytes = json.dumps(definition).encode("ascii")
        definition_base64 = base64.b64encode(definition_bytes)
        payload_base64 = base64.b64encode(payload)
        create_tx = await wallet.create_and_sign_tx(
            CreateTxOptions(
                msgs=[
                    MsgCreateJob(wallet.key.acc_address, {
                        "ID": job_id,
                        "owner": "",
                        "routing": {
                            "chainType": chain_type,
                            "chainReferenceID": chain_reference_id
                        },
                        "definition": definition_base64,
                        "payload": payload_base64,
                        "isPayloadModifiable": True,
                        "permissions": {
                            "whitelist": [],
                            "blacklist": []
                        },
                        "triggers": [],
                        "address": ""
                    })
                ]
            )
        )
        create_tx_result = await self._c.tx.broadcast(create_tx)
        return create_tx_result


class JobSchedulerAPI(AsyncJobSchedulerAPI):
    @sync_bind(AsyncJobSchedulerAPI.create_job)
    def create_job(
        self,
        wallet: Wallet,
        job_id: str,
        contract_address: str,
        abi: dict,
        payload: str,
        chain_type: str,
        chain_reference_id: str
    ) -> BlockTxBroadcastResult:
        pass

    create_job.__doc__ = AsyncJobSchedulerAPI.create_job.__doc__
