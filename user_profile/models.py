from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager)




# Define custom User manager. 
class AirpactUserManager(BaseUserManager):
	
	# define custom create user 
	def create_user(self, email, name, password = None):
		if not email:
			raise ValueError('Users must have valid email')

		if not name:
			raise ValueError('Users must have a name!')

		if not password:
			raise ValueError('Users must have a valid password!')

		user = self.model(username=name)
		user.set_password(password)
		user.save(using=self._db)

		return user

	# I believe a super user is a user with admin priviledges
	def create_superuser(self, email, password):
		user = self.create_user(email=email, username = name, password = password)
		user.is_admin = True;
		user.is_superuser = True;
		user.save(using=self._db)

		return user


# This is a custom user/userprofile class
class AirpactUser(AbstractBaseUser):
	username = models.CharField(max_length=254, unique=True)
	#password = models.CharField(max_length=254)
	bio = models.TextField(max_length=1000, null=True, blank=True)
	first_name = models.CharField(max_length=30,null=False, blank=True)
	last_name = models.CharField(max_length=30, null=False, blank=True)
	email = models.EmailField(blank=True)
	is_custom_admin = models.BooleanField(default = False)
	is_certified = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	bob = models.BooleanField(default= False)
	objects = AirpactUserManager()

	#required to implement
	is_active = models.BooleanField(default=True)

	#required to implement
	USERNAME_FIELD = 'username'
   	
   	#TODO: make this a longer list, required to implement
   	REQUIRED_FIELDS = ['email']

   	def get_full_name():
   		return (first_name + last_name)

   	def get_short_name():
   		return first_name

class AuthToken(models.Model):
	token = models.TextField(max_length =22, unique=True, primary_key=True)
	issue_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.token

