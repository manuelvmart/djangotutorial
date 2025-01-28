from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


from django.contrib import admin
  
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    #is_paused = models.BooleanField(default=False)
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone_now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.creator = get_user_model().objects.first()
        super().save(*args, **kwargs)

    def answers(self):
        return self.answer_set.all()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.voter.username}'s answer to {self.question.question_text}"
    
    def save(self, *args, **kwargs):
        if not self.pk: 
            self.creator = get_user_model().objects.first()
        super().save(*args, **kwargs)



class Not_allowed(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
 
    def __str__(self):
        return self.request

