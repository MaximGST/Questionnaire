from django.shortcuts import render
from rest_framework import generics
from rest_framework.utils import serializer_helpers
from cars.serializers import (
    DetailSerializer, 
    ListSerializer, 
    QuestionSerializer, 
    AnswerQuestionSerializer, 
    SurveySerializer, 
    AnswerSerializer,
    ResponderSerializer,
)
from .models import Question, Responder, Survey, SurveyResponder, AnswerQuestion, Answer
from cars.permission import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CreateView(generics.CreateAPIView):
    queryset = SurveyResponder.objects.all()
    serializer_class = DetailSerializer
    


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailSerializer
    queryset = SurveyResponder.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


#Вопросы
class QuestionView(generics.CreateAPIView):
    model = Question
    serializer_class = QuestionSerializer


#Ответы
class AnswerView(generics.CreateAPIView):
    model = Answer
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


#Ответы на вопросы
class AnswerQuestionView(generics.CreateAPIView):
    model = AnswerQuestion
    serializer_class = AnswerQuestionSerializer


#Создание опросов
class SurveyView(generics.CreateAPIView):
    model = Survey
    serializer_class = SurveySerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = Responder.objects.all()
    serializer_class = ResponderSerializer


#Список пользователей
class ListView(generics.ListAPIView):
    serializer_class = ListSerializer
    queryset = Responder.objects.all()
    permission_classes = (IsAuthenticated, )


#Пользователи
class UserView(generics.CreateAPIView):
    serializer_class = ResponderSerializer
    queryset = Responder.objects.all()