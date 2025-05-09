from rest_framework import serializers
from .models import CustomUser


# Serializers define the API representation.
class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

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
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance