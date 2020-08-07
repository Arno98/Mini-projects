
#A class is created to encode the order data and create the signature.
class PostData():
	
	def __init__(self, order=None):
		"""If during a call to views.py you transmit your order, data with your order is generated. 
		If you do not pass on your order, then test data are generated."""
		if order:
			self.order = order
			self.private_key = settings.PRIVATE_KEY
			self.data = {"public_key": settings.PUBLIC_KEY, "version": 3, "action": "pay", "amount": str(self.order.get_total_cost()), "currency": "UAH", "description": "Оплата заказа №" + str(self.order.id), "order_id": self.order.id, "result_url": "https://your-site.com/result_page" + str(self.order.id) + "/"}
		else:
			self.private_key = 'YOUR TEST PRIVATE KEY'
			self.data = {"public_key": "YOUR TEST PUBLIC KEY", "version": 3, "action": "pay", "amount": "5", "currency": "UAH", "description": "TEST", "order_id": 10, "result_url": "https://your-site.com/result_page/"}
	
	#The encoded data of your order is generated	
	def _data(self):
		self.encode_data = base64.b64encode(json.dumps(self.data).encode("utf-8")).decode("utf-8")
		return self.encode_data
	
	#The encoded signature of your data is generated	
	def _signature(self):
		signature = (self.private_key + self.encode_data + self.private_key).encode("utf-8")
		encode_signature = base64.b64encode(hashlib.sha1(signature).digest()).decode("ascii")
		return encode_signature

#A class is created to decrypt the data and sign the LiqPay response (when specifying result_url or server_url).		
class GetData():
	
	def __init__(self, data):
		self.private_key = settings.PRIVATE_KEY
	
	#Forming the signature of LiqPay response	
	def str_to_sign(self):
		data_sign = self.private_key + self.data + self.private_key
		sign = base64.b64encode(hashlib.sha1(data_sign.encode("utf-8")).digest()).decode("ascii")
		return sign
	
	#Decoding LiqPay response data into json data	
	def decode_data_from_str(self):
		data_from_str = json.loads(base64.b64decode(self.data).decode('utf-8'))
		return data_from_str
