from django.contrib import admin
from .models import Survey, Answer, Question, AnswerQuestion, SurveyResponder, Responder
# Register your models here.

admin.site.register(Survey)
admin.site.register(SurveyResponder)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(AnswerQuestion)
admin.site.register(Responder)