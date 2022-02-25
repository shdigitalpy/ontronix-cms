from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets 
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.reverse import reverse
from django.http import Http404
from rest_framework import status, generics
from django.core import serializers
from rest_framework.generics import UpdateAPIView


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (AllowAny,)

class FileView(viewsets.ModelViewSet):
	queryset = File.objects.all()
	serializer_class = FileSerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

class ProductView(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class BlogView(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

class ServiceView(viewsets.ModelViewSet):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer
	

class SectionView(viewsets.ModelViewSet):
	queryset = Section.objects.all()
	serializer_class = SectionSerializer

class PartnerView(viewsets.ModelViewSet):
	queryset = Partner.objects.all()
	serializer_class = PartnerSerializer

class JobView(viewsets.ModelViewSet):
	queryset = Job.objects.all()
	serializer_class = JobSerializer

class PageView(viewsets.ModelViewSet):
	queryset = Page.objects.all()
	serializer_class = PageSerializer



class GalleryView(viewsets.ModelViewSet):
	queryset = Gallery.objects.all()
	serializer_class = GallerySerializer
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)
