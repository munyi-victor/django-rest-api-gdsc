from django.shortcuts import render

# importing rest_framework class
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import QuestionsSerializer
from .models import Question

class AllQuestionsView(APIView):
  def get(self, request, *args, **kwargs):
    quiz_qs = Question.objects.all()
    serializer = QuestionsSerializer(quiz_qs, many=True,)
        
    return Response(serializer.data)
  
  def post(self, request, *args, **kwargs):
    serializer = QuestionsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status=status.H)