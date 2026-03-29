from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Question, Attempt, Leaderboard
from .serializers import (UserSerializer, RegisterSerializer, 
                          QuestionSerializer, submitAttemptSerializer, 
                          LeaderboardSerializer)
import random

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class QuestionListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        questions = list(Question.objects.all())
        if len(questions) > 10:
            questions = random.sample(questions, 10)
        else:
            random.shuffle(questions)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class SubmitAttemptView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = submitAttemptSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            question_id = serializer.validated_data['question_id']
            selected_answer = serializer.validated_data['selected_answer']

            try:
                question = Question.objects.get(id=question_id)
            except Question.DoesNotExist:
                return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

            is_correct = (question.correct_answer == selected_answer)

            # Record attempt
            Attempt.objects.create(
                user=user,
                question=question,
                selected_answer=selected_answer,
                is_correct=is_correct
            )

            # Update stats
            xp_gained = 0
            if is_correct:
                xp_gained = 10
                user.add_xp(xp_gained)
                user.streak += 1
                
                # Update Leaderboard
                leaderboard, _ = Leaderboard.objects.get_or_create(user=user)
                leaderboard.score = user.total_score
                leaderboard.save()
            else:
                user.streak = 0
            
            user.save()

            # explanation why correct answer is returned: To show instant feedback
            return Response({
                "is_correct": is_correct,
                "correct_answer": question.correct_answer,
                "xp_gained": xp_gained,
                "new_xp": user.xp,
                "new_level": user.level,
                "new_streak": user.streak
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Leaderboard.objects.all().order_by('-score')[:10]
    serializer_class = LeaderboardSerializer

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
