from rest_framework import serializers
from models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'create_time', 'name', 'tel',
                  'pwd', 'user_img', 'car_plate','money')



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','create_time', 'appoint_time', 'startSite', 'endSite',
                  'payer', 'payer_tel', 'picker','picker_tel','duration','distance')


