from web3 import Web3

#define Eth networks and addresses
networks = {
    "Mainnet": {
        "url": "https://mainnet.infura.io/v3/your_project_id",
        "eth_address": "qucknode.eth"
    },
    "Goerli": {
        "url": "https://goerli.infura.io/v3/your_project_id",
        "eth_address": "qucknode.eth"
    },
    "Sepolia": {
        "url": "https://sepolia.blockchain.azure.com:3200/<your-Azure-blockchain-workspace-ID>",
        "eth_address": "qucknode.eth"
    }
}

#connect to Eth networks and get latest block numbers
w3_networks = {}
blocks = {}
for network, config in networks.items():
    w3_networks[network] = Web3(Web3.HTTPProvider(config['url']))
    blocks[network] = w3_networks[network].eth.block_number

#balance and transaction counts
for network, w3 in w3_networks.items():
    eth_address = networks[network]['eth_address']
    resolved_address = w3.ens.resolve(eth_address)
    balance = w3.eth.get_balance(resolved_address, block_identifier=blocks[network])
    tr_count = w3.eth.get_transaction_count(resolved_address, block_identifier=blocks[network])
    print(f"{network}: Latest block number = {blocks[network]}, Balance = {balance}, Transaction count = {tr_count}")
