from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
#set up to show the question text vs just the object 
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # createing association with the question using foreignKey
    #if a question is deleted all of its choices will also be deleted
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text