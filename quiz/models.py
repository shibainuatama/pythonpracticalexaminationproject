from django.db import models

# Create your models here.
class Book(models.Model):
    chapter = models.IntegerField()
    title = models.CharField(max_length=20)
    link = models.BooleanField()
    
    def __str__(self):
        return str(self.chapter) + " " + self.title

class Quiz(models.Model):
    chapter = models.IntegerField()
    number =  models.IntegerField()
    about = models.TextField()
    question = models.TextField()
    optionA = models.TextField()
    optionB = models.TextField()
    optionC = models.TextField()
    optionD = models.TextField()
    correctanswer = models.CharField(max_length=5)
    explanation = models.TextField()
    
    def __str__(self):
        return str(self.chapter) + "-" + str(self.number) + " " + self.about
