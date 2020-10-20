import json
import random

import requests
class request_methods:
	def __init__(self):

		self.headers = {
			'content-type': 'application/json','token':''}

	def get(self, url):

		try:
			r = requests.get(url=url, headers=self.headers)
			response = json.loads(r.text)

		except BaseException as e:
			print("get请求错误，错误原因：%s" % e)

	def post(self, url, params):

		data = json.dumps(params)
		try:
			r = requests.post(url=url, json=data, headers=self.headers)
			response = json.loads(r.text)

		except BaseException as e:
			print("post请求错误，错误原因：%s" % e)

	def create_phone(self):
		second = [3, 4, 5, 7, 8][random.randint(0, 4)]
		third = {3: random.randint(0, 9),
		         4: [5, 7, 9][random.randint(0, 2)],
		         5: [i for i in range(10) if i != 4][random.randint(0, 8)],
		         7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
		         8: random.randint(0, 9),
		         }[second]
		suffix = random.randint(9999999, 100000000)
		num = "1{}{}{}".format(second, third, suffix)
		return num