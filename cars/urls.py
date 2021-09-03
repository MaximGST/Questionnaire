from django.urls import path
from cars.views import *


app_name = 'questionnaire'

urlpatterns = [
    path('create/', CreateView.as_view()),
    path('all/', ListView.as_view()),
    path('detail/<int:pk>', DetailView.as_view()),
    path('question/', QuestionView.as_view()), 
    path('answerquestion/', AnswerQuestionView.as_view()),
    path('survey/', SurveyView.as_view()),
    path('answer/', AnswerView.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('user/', UserView.as_view()),
]

