from rest_framework import serializers

from podcast.models import Podcast


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['id', 'name', 'description', 'link', 'leading_dr']

    def create(self, validated_data):
        try:
            return Podcast.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})