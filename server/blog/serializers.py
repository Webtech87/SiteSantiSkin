from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'date_posted']
        read_only_fields = ['author', 'date_posted']

    def create(self, validated_data):
        try:
            user = self.context['request'].user
            if not user or user.is_anonymous :
                return serializers.ValidationError({"detail": "You do not have permission to perform this action."})
            validated_data['author'] = user
            return Post.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})