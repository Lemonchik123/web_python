from web3 import Web3
from eth_account import Account
import secrets
import traceback

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/")) #Нода bsc (сеть)
print (web3.isConnected())

#переменные
address = "адрес"
amount = web3.eth.getBalance(address)

#получение баланса бнб (wei)
balance_wei = web3.eth.get_balance(address)
print(balance_wei)

#получения блока
block_number = web3.eth.get_block_number()
print(block_number)


#cоздание кошелька
priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("Приват ключ:", private_key)

acct = Account.from_key(private_key)
print("Address:", acct.address)


#узнать актуальный газ
gas_gwei = web3.eth.gas_price
gas_eth = (gas_gwei) / (10**9)
print("актуальный газ на перевод: =", (gas_eth))



#создание большого кол-ва кошельков
for i in range(1,2):
            priv = secrets.token_hex(32)
            private_key = "0x" + priv
            address = Account.from_key(private_key)
            
            f = open("seed.txt", 'a')
            f.write(f'{private_key} \n')
            f.close()
            
            acc = Account.from_key(private_key)
            
            #адрес этих кошельков
            f = open("address.txt", 'a')
            f.write(f'{acc.address} \n')
            f.close
            
            print("номер кошелька =", (i))


print("complete")





    
            

            









