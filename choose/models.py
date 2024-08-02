from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    answer_A = models.TextField()
    answer_B = models.TextField()

class Comment(models.Model):
    answer = models.TextField()
    comment = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Reply(models.Model):
    reply = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)