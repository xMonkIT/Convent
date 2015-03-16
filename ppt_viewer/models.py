from django.db import models

# Create your models here.
class Section(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Thesis(models.Model):
	title = models.CharField(max_length=100)
	section = models.ForeignKey(Section)

	def __str__(self):
		return self.title

class Slide(models.Model):
	image = models.FileField(upload_to='slides')
	num = models.IntegerField(max_length=10)
	thesis = models.ForeignKey(Thesis)

