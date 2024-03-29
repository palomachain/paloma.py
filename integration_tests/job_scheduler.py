import asyncio

import uvloop
from web3 import Web3
from web3.contract import Contract

from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.key.mnemonic import MnemonicKey
import time


async def main():
    paloma = AsyncLCDClient(
        url="https://lcd.testnet.palomaswap.com/", chain_id="paloma-testnet-15"
    )
    paloma.gas_prices = "0.01ugrain"

    acc = MnemonicKey(
        mnemonic="notice oak worry limit wrap speak medal online prefer cluster roof addict wrist behave treat actual wasp year salad speed social layer crew genius"
    )

    test1 = paloma.wallet(acc)

    job_id = "test102"
    contract_address = "0x1f576F2021b6EBdF229750f54fDFd31206141E65"
    abi = [
        {
            "inputs": [],
            "name": "retrieve",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [{"internalType": "uint256", "name": "num", "type": "uint256"}],
            "name": "store",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    creator = test1.key.acc_address
    signers = [test1.key.acc_address]
    payload = "6057361d00000000000000000000000000000000000000000000000000000000000000ea"
    chain_type = "evm"
    chain_reference_id = "bnb-main"
    result = await paloma.job_scheduler.create_job(
        test1, job_id, contract_address, abi, payload, chain_type, chain_reference_id, creator, signers
    )
    print(result)
    time.sleep(10)
    job_id = "test102"
    payload = "6057361d00000000000000000000000000000000000000000000000000000000000000ea"
    result = await paloma.job_scheduler.execute_job(test1, job_id, payload, creator, signers)
    print(result)
    await paloma.session.close()


def payload(contract_address: str, abi: dict, function_name: str, parameters: list):
    infura_key: str = ""
    node: str = "https://mainnet.infura.io/v3/" + infura_key
    w3: Web3 = Web3(Web3.HTTPProvider(node))
    smart_contract: Contract = w3.eth.contract(address=contract_address, abi=abi)
    return smart_contract.encodeABI(function_name, parameters)[2:]


uvloop.install()
asyncio.run(main())
