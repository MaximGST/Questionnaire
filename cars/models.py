from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import datetime, timedelta

# class Car(models.Model):
#     vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
#     color = models.CharField(verbose_name='Color', max_length=64)
#     brand = models.CharField(verbose_name='Brand', max_length=64)
#     CAR_TYPES = (
#         (1, 'Седан'),
#         (2, 'Хэчбек'),
#         (3, 'Универсал'),
#         (4, 'Купе'),
#     )
#     car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES)
#     user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


class Survey(models.Model):
    title = models.CharField('Название опроса', max_length=200)
    start_date = models.DateTimeField('Дата и время начало опроса', default=datetime.now())
    end_date = models.DateTimeField('Дата и время окончание опроса', default=datetime.now()+timedelta(days=10))
    description = models.TextField('Описание опроса')
    create_at = models.DateTimeField('Дата создания опроса', auto_created=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['-create_at']


class Answer(models.Model):
    responder = models.ForeignKey('SurveyResponder', on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return f'{self.responder} -> {self.question}'

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'
        ordering = ['-id']



class Question(models.Model):
    QUESTION_TYPE = (
        ('1', 'Ответ текстом'),
        ('2', 'Ответ с выбором одного варианта'),
        ('3', 'Ответ с выбором нескольких вариантов')
    )

    text = models.TextField('Вопрос')
    question_type = models.CharField('Тип вопроса', choices=QUESTION_TYPE, max_length=150)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')

    def __str__(self):
        return f'{self.survey} -> {self.text}'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-id']


class AnswerQuestion(models.Model):
    text = models.TextField('Ответ к вопросу')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-id']


class SurveyResponder(models.Model):
    responder = models.ForeignKey('Responder', on_delete=models.CASCADE, verbose_name='Пользователь')
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос')
    answers = models.ManyToManyField(Question, through=Answer, verbose_name='Ответы пользователя')

    def __str__(self):
        return f'{self.responder} -> {self.survey}'

    class Meta:
        verbose_name = 'Опрос который прощел пользователь'
        verbose_name_plural = 'Опросы которые прощел пользователь'
        ordering = ['-id']


class Responder(models.Model):
    ip = models.CharField('ip пользователя', max_length=50)
    survey = models.ManyToManyField(Survey, verbose_name='Опросы', through=SurveyResponder)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']

