from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from .permissions import PostPermitions

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [PostPermitions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
