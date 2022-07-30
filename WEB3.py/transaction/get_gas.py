from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/")) #Нода bsc (сеть)

gas_gwei = web3.eth.gas_price
print(web3.fromgwei(gas_gwei, 'ether'))
