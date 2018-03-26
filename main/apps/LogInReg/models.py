from __future__ import unicode_literals
from django.db import models
import bcrypt
from views import *

hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())
print hash1
# $2b$12$5u.QgExiKyaV1szrvEfbE.sc7tf7hWcE0/AJfivWmWuMxhyTUygm2
# $2b$12$YcjfvChLPyRbyhWpmff.6eEzbMhutcMmWvfnpm6lg5BxuMTt.ABYy
# Create your models here.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Name should be more than 2 characters"
        if len(postData['email']) < 2:
            errors["email"] = "Email should be more than 2 characters"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()

class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# class password(models.Model):
#     password = 
#     hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())


class createUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    # password = bcrypt.hashpw(session['cPassword'].encode(), bcrypt.gensalt())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()



class Stuff(models.Model):
    item = models.CharField(max_length=255)
    add_by = models.ForeignKey(User, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
