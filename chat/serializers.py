# from django.contrib.auth.models import User
from accounts.models import ProfcessUser
from rest_framework import serializers
from chat.models import Message
#
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """For Serializing User"""
    password = serializers.CharField(write_only=True)
    online = serializers.ReadOnlyField(source='userprofile.online')

    class Meta:
        model = ProfcessUser
        fields = ['id', 'username', 'password', 'online']
#
# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=ProfcessUser.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=ProfcessUser.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
