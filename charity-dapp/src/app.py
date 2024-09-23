from flask import Flask, jsonify, request
from web3 import Web3
import json

app = Flask(__name__)

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load the contract
with open('Charity.json') as f:
    contract_json = json.load(f)
    abi = contract_json['abi']

contract_address = '0xYourContractAddressHere'
contract = web3.eth.contract(address=contract_address, abi=abi)

@app.route('/donate', methods=['POST'])
def donate():
    data = request.json
    donor_address = data['address']
    amount = web3.toWei(data['amount'], 'ether')

    # Send donation transaction
    txn = contract.functions.donate().transact({
        'from': donor_address,
        'value': amount
    })

    receipt = web3.eth.wait_for_transaction_receipt(txn)
    return jsonify({"message": "Donation successful", "txn_hash": receipt.transactionHash.hex()})

@app.route('/balance', methods=['GET'])
def get_balance():
    balance = contract.functions.getBalance().call()
    return jsonify({"balance": web3.fromWei(balance, 'ether')})

if __name__ == '__main__':
    app.run(debug=True)
