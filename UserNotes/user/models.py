from django.db import models
import datetime


# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_name = models.CharField(max_length=40)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     phone_num = models.CharField(max_length=10, unique=True)
#     address = models.TextField(max_length=300)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=20)
#     is_active = models.BooleanField(default=False)
#     gender = models.CharField(max_length=20)
#     db_created = models.DateTimeField(default=datetime.datetime.now)
#
#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)
