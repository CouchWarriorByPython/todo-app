from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'


class TodoForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'complete', 'date_create']


class UserSerializer(serializers.ModelSerializer):
    todos = TodoForUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'todos']
