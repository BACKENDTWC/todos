from django.db import models
import uuid
from authuser.models import User

# Create your models here.
## For Data Creation





class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length= 200)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    hire = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return self.first_name
    



