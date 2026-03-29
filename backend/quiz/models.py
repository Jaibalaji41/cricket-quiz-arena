from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    streak = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    
    def add_xp(self, amount):
        self.xp += amount
        self.total_score += amount
        self.level = (self.xp // 100) + 1
        self.save()

class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    CATEGORY_CHOICES = [
        ('IPL', 'IPL'),
        ('World Cup', 'World Cup'),
        ('Player', 'Player'),
    ]

    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='IPL')

    def __str__(self):
        return self.text

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=1)
    is_correct = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text[:20]} - {'Correct' if self.is_correct else 'Wrong'}"

class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
