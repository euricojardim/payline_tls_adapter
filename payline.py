## Payline DOCS
## https://payline.atlassian.net/wiki/spaces/DT/pages/24248460/Endpoints
##

import datetime
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport
from zeep.helpers import serialize_object


# WSDL = '20180319.wsdl'
# WSDL = 'https://homologation.payline.com/V4/services/WebPaymentAPI?wsdl'
# WSDL = 'https://services.payline.com/V4/services/WebPaymentAPI?wsdl'
# WSDL = 'http://www.payline.com/wsdl/v4_0/homologation/WebPaymentAPI.wsdl'
WSDL = 'v4.43.wsdl'


def do_web_payment(merchant_id, access_key, contract_number,
		return_url, cancel_url, notification_url, amount, reference,
		currency=978, mode='CPT', action=101):

	session = Session()
	session.auth = HTTPBasicAuth(merchant_id, access_key)
	client = Client(WSDL, transport=Transport(session=session))
	service = client.create_service(
	    '{http://impl.ws.payline.experian.com}WebPaymentAPISoapBinding',
	    'https://services.payline.com/V4/services/WebPaymentAPI')

	payment_type = client.get_type('ns1:payment')
	payment = payment_type(amount=amount, currency=currency, action=action, mode=mode, contractNumber=contract_number)
	date_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
	order_type = client.get_type('ns1:order')
	order = order_type(ref=reference, country='PT', amount=amount, currency=currency, date=date_str)
	contractlist_type = client.get_type('ns1:selectedContractList')
	contractlist = contractlist_type(contract_number)
	privatedatalist_type = client.get_type('ns1:privateDataList')
	privatedata_type = client.get_type('ns1:privateData')
	privatedata = privatedata_type(key='order_id', value=reference)
	privatedatalist = privatedatalist_type(privatedata)

	response = service.doWebPayment(version=4, payment=payment, returnURL=return_url, cancelURL=cancel_url, order=order,
		notificationURL=notification_url, selectedContractList=contractlist, privateDataList=privatedatalist,
		languageCode='pt')

	return serialize_object(response)


def get_web_payment_details(merchant_id, access_key, token):

	session = Session()
	session.auth = HTTPBasicAuth(merchant_id, access_key)
	client = Client(WSDL, transport=Transport(session=session))
	service = client.create_service(
	    '{http://impl.ws.payline.experian.com}WebPaymentAPISoapBinding',
	    'https://services.payline.com/V4/services/WebPaymentAPI')

	response = service.getWebPaymentDetails(version=4, token=token)
	return serialize_object(response)

