from rest_framework import serializers
from .models import User, Question, Attempt, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'xp', 'level', 'streak', 'total_score']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        Leaderboard.objects.create(user=user, score=0)
        return user

import random

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'text', 'difficulty', 'category', 'options']
        
    def get_options(self, obj):
        options = [
            {'key': 'A', 'text': obj.option_a},
            {'key': 'B', 'text': obj.option_b},
            {'key': 'C', 'text': obj.option_c},
            {'key': 'D', 'text': obj.option_d},
        ]
        return options

class submitAttemptSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    selected_answer = serializers.ChoiceField(choices=['A', 'B', 'C', 'D'])

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    class Meta:
        model = Leaderboard
        fields = ['username', 'score']
