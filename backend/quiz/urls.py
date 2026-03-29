from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, QuestionListView, SubmitAttemptView, 
    LeaderboardView, ProfileView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('questions/', QuestionListView.as_view(), name='questions-list'),
    path('submit/', SubmitAttemptView.as_view(), name='submit-attempt'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
