#coding:utf-8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect,csrf_exempt
# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from rest_framework import viewsets, status
from serializers import *
from models import *
from rest_framework.decorators import api_view
# from models import User
import json

class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet表的增删改查
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        query_params = {}
        for k,v in self.request.query_params.iteritems():
            query_params[k] = v
        queryset = queryset.filter(**query_params)
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    """
    OrderViewSet表的增删改查
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        print request.FILES['head_img'],request.POST.get('user_id')
        # if 'head_img' in request.FILES:
        upload_file = request.FILES['head_img']
        user_id = request.POST.get('user_id')
        user = User.objects.get(id=user_id)
        print upload_file,user_id
        newfile = Headimage(img=upload_file,user=user)
        newfile.save()
        User.objects.filter(id=user_id).update(user_img=newfile.img.url)
        return HttpResponse(json.dumps({'result':'success','url':newfile.img.url}))
        # return HttpResponse(json.dumps({'result':'success','url':'newfile.uploadfile.url'}))
    else:
        return HttpResponse(json.dumps({'result':'error','code':'不支持的HTTP方法'}))