from rest_framework import serializers
from ..posts.models import Group, Post


class GroupSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField()

    class Meta:
        fields = ('id', 'title', 'slug', 'description')

        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    group = GroupSerializer()

    class Meta:
        fields = ('id', 'text', 'author', 'group', 'image', 'pub_date')

        model = Post


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('author', 'post', 'text')
