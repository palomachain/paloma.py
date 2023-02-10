import json
import betterproto
from typing import Union
from dataclasses import dataclass
from paloma_sdk.core import AccAddress

@dataclass(eq=False, repr=False)
class Routing(betterproto.Message):
    """
    """
    chainType: str = betterproto.string_field(1)
    chainReferenceID: str = betterproto.string_field(2)

@dataclass(eq=False, repr=False)
class Job(betterproto.Message):
    """
    """
    ID: str = betterproto.string_field(1)
    owner: str = betterproto.string_field(2)
    routing: Routing = betterproto.message_field(3)
    definition: str = betterproto.string_field(4)
    payload: str = betterproto.string_field(5)
    isPayloadModifiable: bool = betterproto.bool_field(6)
    permissions: bytes = betterproto.bytes_field(7)
    triggers: bytes = betterproto.bytes_field(8)
    address: str = betterproto.string_field(9)


@dataclass(eq=False, repr=False)
class MsgCreateJob(betterproto.Message):
    """
    MsgExecuteContract submits the given message data to a smart contract
    """

    # Job creator
    creator: str = betterproto.string_field(1)
    # Job json
    job: Job = betterproto.message_field(2)
    # Msg json encoded message to be passed to the contract

def parse_msg(msg: Union[dict, str, bytes]) -> dict:
    if type(msg) is dict:
        return msg
    return json.loads(msg)