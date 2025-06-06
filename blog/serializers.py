from rest_framework import serializers
from .models import Post, Category, Tag, Comment
from django.contrib.auth.models import User  # ✅ Import User model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# ✅ Custom Serializer for Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # ✅ Now returns an object (not string)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
