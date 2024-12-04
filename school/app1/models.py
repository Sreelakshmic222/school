from django.db import models

# Log model to keep track of sign-ins
class Log(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=8,default=True)
    signed_in_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Teacher model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    teachers = models.ManyToManyField(Teacher, related_name='students')

    def __str__(self):
        return self.name
