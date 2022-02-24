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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'slug',
            'thumbnail',
            'thumbnail_alt',
            'meta_title',
            'meta_description',
            'price',
            'sort',
        
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


class GallerySerializer(serializers.ModelSerializer):
	class Meta:
		model = Gallery
		fields = (
			'id',
			'image',
			'alt',
		
			)
