# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
# Create your views here.
import mongodb_api
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
userAPI=mongodb_api.userAPI()
orderAPI = mongodb_api.orderAPI()
@api_view(['POST'])
def api_register_user(request):
	response = User().find(request)
	if response:
		return response
	else:
		response = User().insert(request)
	return response

@api_view(['POST'])
def api_update_userinfo_user(request):
	response = User().update(request)
	return response


@api_view(['POST'])
def api_insert_order(request):
	response = Order().insert(request)
	return response

@api_view(['GET'])
def api_get_all_order(request):
	response = Order().find_all(request)
	return response

@api_view(['POST'])
def api_update_order(request):
	response = Order().update_order(request)
	return response

@api_view(['GET'])
def api_get_user_order(request):
	response = Order().find_user(request)
	return response


class User(object):
	def __init__(self):
	    self.function_name = 'user'

	def insert(self,request):
		data = {}
		data['tel'] = request.data.get('tel')
		userAPI.add_user_info(data)
		# User().find(request)
		res = userAPI.get_user__info(request.data.get('tel'))
		for item in res:
			item['_id'] = str(item['_id'])
		return HttpResponse(json.dumps(res))
		

	def find(self,request):
		tel = request.data.get('tel')
		data = userAPI.get_user__info(tel)
		print 'data',data
		if not data or str(data)=='[]':
			print '---'
			return None
		for item in data:
			item['_id'] = str(item['_id'])
		print '>>>'
		return HttpResponse(json.dumps(data))

	def update(self,request):
		_id = request.data.get('_id')
		tel = request.data.get('tel')
		sex = request.data.get('sex')
		username = request.data.get('username')
		head_img = request.data.get('head_img')
		userAPI.update_user_info(_id, username, tel, sex, head_img)
		return HttpResponse('success')



class Order(object):
	def __init__(self):
	    self.function_name = 'order'

	def insert(self,request):
		data = request.data.get('orderInfo')
		orderAPI.add_order_info(data)
		return HttpResponse('success')
		

	def find_all(self,request):
		data = orderAPI.get_all_order_info()
		if not data or str(data)=='[]':
			return None
		for item in data:
			item['_id'] = str(item['_id'])
		return HttpResponse(json.dumps(data))

	def find_user(self,request):
		tel = request.GET.get('tel')
		print tel
		data = orderAPI.get_user_order_info(tel)
		if not data or str(data)=='[]':
			return None
		for item in data:
			item['_id'] = str(item['_id'])
		return HttpResponse(json.dumps(data))

	def update_order(self,request):
		_id = request.data.get('_id')
		accept_user = request.data.get('accept_user')
		accept_tel = request.data.get('accept_tel')
		accept_car = request.data.get('accept_car')
		accept_header_img = request.data.get('accept_header_img')
		status = request.data.get('status')
		print _id,accept_user,accept_tel,accept_car,accept_header_img
		orderAPI.update_order_info(_id=_id, accept_user=accept_user, accept_tel=accept_tel, accept_img=accept_header_img,accept_car=accept_car,status=status)
		return HttpResponse('success')

