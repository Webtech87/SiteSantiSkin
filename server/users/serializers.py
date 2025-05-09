from rest_framework import serializers
from .models import CustomUser


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name','last_name' ,'phone','accepted_terms', "password"]

    def create(self, validated_data):
        psw = validated_data['password']
        user = CustomUser(**validated_data)
        user.set_password(psw)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.save()
        return instance
