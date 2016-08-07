from django.db import models

# Create your models here.
class Bookmark(models.Model): 
	name = models.CharField(max_length=50)
	link = models.CharField(max_length=30)

	def __str__(self):
		return self.name