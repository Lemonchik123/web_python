from web3 import Web3
import json

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/")) #Нода bsc (сеть)
print (web3.isConnected())

account_1 ="" #адрес нашего кошелька
account_2 ="" #адрес, на который хотим перевести

private_key =''


# get the nonce
nonce = web3.eth.getTransactionCount(account_1)

#build transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1,'ether'),
    'gas':200000,
    'gasPrice':web3.toWei('50','gwei')

}


signed_tx = web3.eth.account.signTransaction(tx,private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaccion hash
print("https://bscscan.com/tx/" + (web3.toHex(tx_hash)))