from api_tools.request_method import request_methods

req = request_methods()
class api_lists:
	test_host = 'http://'
	login_url = test_host+'/user/Auth/userLogin'
	user_account = '18502338722'
	password = 'BE56E057F20F883EE10ADC3949BA59AB'
	unionId = ''
	verifyCode = ''
	deviceNumber = req.create_phone()
	@classmethod
	def old_user_login(self):
		old_user_params ='?unionId='+self.unionId+'&account='+self.user_account\
		+'&password='+self.password+'&verifyCode='+self.verifyCode+'&deviceNumber='+self.deviceNumber
		respon= req.get(url=self.login_url+old_user_params)
		print(respon)
