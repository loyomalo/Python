from web3 import Web3

# Connect to Ethereum node (replace with your Infura or Alchemy URL)
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Check connection
if web3.is_connected():
    print("Connected to Ethereum!")
else:
    print("Connection failed.")