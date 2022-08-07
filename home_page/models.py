from django.contrib.auth.models import User
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    department_head = models.ForeignKey(User, on_delete=models.CASCADE)
    about_department = models.TextField()

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    feedback_id = models.IntegerField(primary_key=True)
    feedback = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    forwarded_to = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.feedback_id)
