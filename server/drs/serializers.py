from rest_framework import serializers
from .models import Dr

class DrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dr
        fields = ['first_name', 'last_name', 'email', 'is_staff', 'dr_license']
