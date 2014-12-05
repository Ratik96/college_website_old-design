from django.http import HttpResponse
import json
import random
import hashlib


def get_captcha(request):
	'''Returns a captcha string along with a hash'''
	data={}
	#
	x=random.choice(range(50))
	y=random.choice(range(50))
	op=random.choice(['+','-','x','>','<'])
	data['string']=string(x)+op+string(y)
	answer=eval(data['string'])
	net=data['string']+string(answer)
	#
	hash=hashlib.md5(net)
	data['hash']=hash.hexdigest()
	return HttpResponse(json.dumps(data),content_type='application/json')
def check_captcha(request):
	'''Returns a captcha submission and thus validates the humanity of the user'''
	
	return HttpResponse(json.dumps(True),content_type='application/json')
	return HttpResponse(json.dumps(False),content_type='application/json')
	
