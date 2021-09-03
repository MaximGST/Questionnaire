from django.db.models import query
from rest_framework import fields, serializers
from .models import Answer, Survey, SurveyResponder, Question, AnswerQuestion, Responder


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = '__all__'
        

class DetailSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = SurveyResponder
        fields = '__all__'
        

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestion
        fields = '__all__'

#Опросы
class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


#Пользователи
class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responder
        fields = '__all__'


#Ответы
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'