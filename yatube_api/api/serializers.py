from rest_framework import serializers
from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = 'id'

        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'group')

        model = Post


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = 'text'

        model = Comment
