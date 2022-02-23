from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now


PAYMENT_CHOICES = (
	('I', 'Invoice*'),
	('C', 'Credit Card'),
	)


class Gallery(models.Model):
	image = models.ImageField(null=True, blank=True)
	alt = models.CharField(max_length=255, null=True, blank=True,)

	def img_alt(self):
		return self.title + ' // ' + self.alt

class Section(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	text = models.TextField(max_length=2000, null=True, blank=True,)

	def __str__(self):
		return self.name

class Page(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	section = models.ManyToManyField(Section, related_name='page_sections', blank=True)

	def __str__(self):
		return self.name


class File(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	alt = models.CharField(max_length=255, null=True, blank=True,)
	file = models.FileField(null=True, blank=True, upload_to="pdf/")

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	slug = models.SlugField(max_length=255,null=True, blank=True,)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="products")
	thumbnail_alt = models.CharField(max_length=255, null=True, blank=True,)
	meta_title = models.CharField(max_length=255, null=True, blank=True,)
	meta_description = models.CharField(max_length=255, null=True, blank=True,)
	price = models.FloatField(null=True, blank=True,)
	sort = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name
		


	


		


