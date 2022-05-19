from django.db import models


class Pic(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField()
	# slug = models.SlugField(null=True)


	def __str__ (self):
		return self.name

class linkedin(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=2000)

	def __str__ (self):
		return self.username


class insta(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=2000)

	def __str__ (self):
		return self.username

class face(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=2000)

	def __str__ (self):
		return self.username
