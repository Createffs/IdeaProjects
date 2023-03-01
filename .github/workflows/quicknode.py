from web3 import Web3
from ens import ENS

#define Eth networks
mainnet = "https://mainnet.infura.io/v3/project_id"
goerli = "https://goerli.infura.io/v3/project_id"
sepolia = "https://sepolia.blockchain.azure.com:3200/<Azure-blockchain-workspace-ID>"
eth_address = "qucknode.eth"

#connect to Eth networks
w3_mainnet = Web3(Web3.HTTPProvider(mainnet))
w3_goerli = Web3(Web3.HTTPProvider(goerli))
w3_sepolia = Web3(Web3.HTTPProvider(sepolia))

#resolve eth address with ENS
ens = ENS.from_web3(w3_mainnet)
resolved_address = ens.address(eth_address)

#latest block numbers
blocks = {
    "Mainnet": w3_mainnet.eth.block_number,
    "Goerli": w3_goerli.eth.block_number,
    "Sepolia": w3_sepolia.eth.block_number,
}

#balance and transaction counts
for network, w3 in [("Mainnet", w3_mainnet), ("Goerli", w3_goerli), ("Sepolia", w3_sepolia)]:
    balance = w3.eth.get_balance(resolved_address, block_identifier = blocks[network])
    tr_count = w3.eth.get_transaction_count(resolved_address, block_identifier = blocks[network])
    print(f"{network}: Latest block number = {blocks[network]}, Balance = {balance}, Transaction count = {tr_count}")

