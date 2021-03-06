from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
