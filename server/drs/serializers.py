from rest_framework import serializers
from .models import Dr

class DrSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)
    dr_license = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False)

    class Meta:
        model = Dr
        fields = ['first_name', 'last_name', 'email', 'dr_license']
