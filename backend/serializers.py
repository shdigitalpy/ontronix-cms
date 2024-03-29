from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import make_password
from django_countries.serializers import CountryFieldMixin
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
   
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
	
	password = serializers.CharField(
		write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'email',
			'password', 
			'first_name', 
			'last_name', 

			)

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'name',
            'alt',
            'file',
           
            )

class BlogGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogGallery
        fields = (
            'id',
            'image',
            'alt',
        
            )

class BlogSerializer(serializers.ModelSerializer):
    blog_gallery = BlogGallerySerializer(
            many=True,
            read_only=True
                    )

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'slug',
            'blog_gallery',
            'meta_title',
            'meta_description',
            'sort',
            'short_description',
            'long_description',
            'date_created',
            'date_updated'
        
            )

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'description',
        
            )

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = (
            'id',
            'image',
            'alt',
        
            )

class ProductSerializer(serializers.ModelSerializer):
    product_gallery = GallerySerializer(
            many=True,
            read_only=True
                    )

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'product_gallery',
            'meta_title',
            'meta_description',
            'price',
            'sort',
            'short_description',
            'long_description'
        
            )

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = (
            'id',
            'name',
            'image',
            'image_alt',
            'sort', 
            'description',
            'short_name'
        
            )


class ServiceGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceGallery
        fields = (
            'id',
            'image',
            'alt',
        
            )

class ServiceSerializer(serializers.ModelSerializer):
    service_gallery = ServiceGallerySerializer(
            many=True,
            read_only=True
                    )
    class Meta:
        model = Service
        fields = (
            'id',
            'name',
            'slug',
            'service_gallery',
            'meta_title',
            'meta_description',
            'price',
            'sort',
            'short_description'
        
            )


class ImageModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModul
        fields = (
            'name',
            'image',
            'alt',
           
            )

class TextModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextModul
        fields = (
            'name',
            'text',
            'text_foreign',
           
            )

class TextImageModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextImageModul
        fields = (
            'name',
            'text',
            'text_foreign',
            'image',
            'link'
           
            )


class SectionSerializer(serializers.ModelSerializer):

    image = ImageModulSerializer(
            many=True,
            read_only=True
                    )

    text = TextModulSerializer(
            many=True,
            read_only=True
                       )

    image_text = TextImageModulSerializer(
            many=True,
            read_only=True
        )

    class Meta:
        model = Section
        fields = (
            'id',
            'name',
            'sort',
            'text',
            'image',
            'image_text'


           
            )

class PageSerializer(serializers.ModelSerializer):

    section = SectionSerializer(
            many=True,
            read_only=True
                    )

    class Meta:
        model = Section
        fields = (
            'name',
            'section',           
            )

