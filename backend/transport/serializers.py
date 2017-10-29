from rest_framework import serializers
from models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'create_time', 'name', 'tel',
                  'pwd', 'user_img')