from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField


PAYMENT_CHOICES = (
	('I', 'Invoice*'),
	('C', 'Credit Card'),
	)


class ImageModul(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	image = models.ImageField(null=True, blank=True, upload_to="image_modul")
	alt = models.CharField(max_length=255, null=True, blank=True,)

	def __str__(self):
		return self.name

class TextModul(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	text = models.TextField(max_length=2000, null=True, blank=True,)
	text_foreign = models.TextField(max_length=2000, null=True, blank=True,)

	def __str__(self):
		return self.name

class TextImageModul(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	text = models.TextField(max_length=2000, null=True, blank=True,)
	text_foreign = models.TextField(max_length=2000, null=True, blank=True,)
	image = models.ImageField(null=True, blank=True, upload_to="image_text_modul")
	link = models.SlugField(max_length=255,null=True, blank=True,)

	def __str__(self):
		return self.name


class Section(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	sort = models.IntegerField(null=True, blank=True)
	text = models.ManyToManyField(TextModul, related_name='section_text', blank=True)
	image = models.ManyToManyField(ImageModul, related_name='section_image', blank=True)
	image_text = models.ManyToManyField(TextImageModul, related_name='section_text_image', blank=True)

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
	short_description = models.TextField(max_length=2000, null=True, blank=True,)
	long_description = RichTextUploadingField(config_name="default",blank=True, null=True)

	def __str__(self):
		return self.name

def get_gallery_filename(instance, filename):
	    title = instance.product.name
	    slug = slugify(title)
	    return "gallery/%s-%s" % (slug, filename)

class Gallery(models.Model):
	product = models.ForeignKey(Product, related_name='product_gallery', default=None, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True, upload_to=get_gallery_filename)
	alt = models.CharField(max_length=255, null=True, blank=True,)

	def __str__(self):
	 	return self.alt

class Service(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	slug = models.SlugField(max_length=255,null=True, blank=True,)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="service")
	thumbnail_alt = models.CharField(max_length=255, null=True, blank=True,)
	meta_title = models.CharField(max_length=255, null=True, blank=True,)
	meta_description = models.CharField(max_length=255, null=True, blank=True,)
	price = models.FloatField(null=True, blank=True,)
	short_description = models.TextField(max_length=2000, null=True, blank=True,)

	sort = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.name

def get_servicegallery_filename(instance, filename):
	    title = instance.service.name
	    slug = slugify(title)
	    return "gallery/service/%s-%s" % (slug, filename)

class ServiceGallery(models.Model):
	service = models.ForeignKey(Service, related_name='service_gallery', default=None, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True, upload_to=get_servicegallery_filename)
	alt = models.CharField(max_length=255, null=True, blank=True,)

	def __str__(self):
	 	return self.alt

class Blog(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True,)
	slug = models.SlugField(max_length=255,null=True, blank=True,)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="products")
	thumbnail_alt = models.CharField(max_length=255, null=True, blank=True,)
	meta_title = models.CharField(max_length=255, null=True, blank=True,)
	meta_description = models.CharField(max_length=255, null=True, blank=True,)
	sort = models.IntegerField(null=True, blank=True)
	short_description = models.TextField(max_length=2000, null=True, blank=True,)
	long_description = RichTextUploadingField(config_name="default",blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

def get_bloggallery_filename(instance, filename):
	    title = instance.blog.title
	    slug = slugify(title)
	    return "gallery/blog/%s-%s" % (slug, filename)

class BlogGallery(models.Model):
	blog = models.ForeignKey(Blog, related_name='blog_gallery', default=None, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True, upload_to=get_bloggallery_filename)
	alt = models.CharField(max_length=255, null=True, blank=True,)

	def __str__(self):
	 	return self.alt


class Partner(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True,)
	short_name = models.CharField(max_length=255, null=True, blank=True,)
	image = models.ImageField(null=True, blank=True, upload_to="products")
	image_alt = models.CharField(max_length=255, null=True, blank=True,)
	sort = models.IntegerField(null=True, blank=True)
	description = models.TextField(max_length=2000, null=True, blank=True,)

	def __str__(self):
		return self.name


class Job(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True,)
	description = RichTextUploadingField(config_name="default",blank=True, null=True)

	def __str__(self):
		return self.title