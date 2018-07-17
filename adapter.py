import json
from flask import Flask, request, jsonify
from . import payline

app = Flask(__name__)

@app.route('/')
def home():
    return 'Ping'

@app.route('/do_web_payment', methods=['POST'])
def do_web_payment():

	merchant_id = request.form.get('merchant_id', '')
	access_key = request.form.get('access_key', '')
	contract_number = request.form.get('contract_number', '')
	return_url = request.form.get('return_url', '')
	cancel_url = request.form.get('cancel_url', '')
	notification_url = request.form.get('notification_url', '')
	amount = request.form.get('amount', 0)
	reference = request.form.get('reference', '')

	response = payline.do_web_payment(merchant_id, access_key, contract_number,
		return_url, cancel_url, notification_url, amount, reference)

	# import pdb; pdb.set_trace()

	return jsonify(response)

@app.route('/get_web_payment_details', methods=['POST'])
def get_web_payment_details():

	merchant_id = request.form.get('merchant_id', '')
	access_key = request.form.get('access_key', '')
	token = request.form.get('token', '')

	response = payline.get_web_payment_details(merchant_id, access_key, token)

	# import pdb; pdb.set_trace()

	return jsonify(response)	

if __name__ == "__main__":
    app.run(host='0.0.0.0')	
