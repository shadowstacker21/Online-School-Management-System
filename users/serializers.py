from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from users.models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta(BaseUserCreateSerializer.Meta):
        model = BaseUserCreateSerializer.Meta.model
        fields = ['id','email','password','profile_picture','first_name','last_name','address','phone_number']
        extra_kwargs = {
            'password': {'write_only': True}   
        }


class UserSerializer(BaseUserSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta(BaseUserSerializer.Meta):
        model = BaseUserSerializer.Meta.model
        ref_name = 'CustomUser'
        fields = ['id','email','profile_picture','first_name','last_name','address','phone_number']

class RoleChangeSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES)
    class Meta:
        model = User
        fields = ['id','role']
