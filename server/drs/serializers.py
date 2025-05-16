from rest_framework import serializers
from .models import Dr

class DrSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_blank=False)
    dr_license = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False)

    class Meta:
        model = Dr
        fields = ['id','first_name', 'last_name', 'email', 'dr_license']

    def validate_dr_license(self, value):
        if Dr.objects.filter(dr_license=value).exists():
            raise serializers.ValidationError("Doctor with this license already exists.")
        return value

    def create(self, validated_data):
        try:
            return Dr.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})