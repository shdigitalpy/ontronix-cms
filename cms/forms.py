from django import forms
from .models import *
from backend.models import *
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

COUNTRY_CHOICES = [
	('S', 'Schweiz'),
	('D', 'Deutschland'),
	('A', 'Österreich'),

	]


class ProduktForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = (
			'sort',
			'name',
			'slug',
			'price',
			'short_description',
			'long_description'
			
			
			
			)

		labels = {
			'name': "Name",
			'slug' : "URL",
			'meta_title' : "SEO-Titel",
			'meta_description' : "SEO-Beschrieb",
			'price' : "Preis",
			'sort' : "Sortierung",
			'short_description': "Kurzbeschrieb",
			'long_description' : "Produktbeschrieb",
		

			
		}

		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
			'slug': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

			'sort': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
			
			
			'meta_title': forms.TextInput(attrs={
				'class': 'form-control',
				}),
			'meta_description': forms.TextInput(attrs={
				'class': 'form-control',
				}),
			

			'short_description': forms.Textarea(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

			
		}

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = (
			'sort',
			'title',
			'slug',
			'meta_title',
			'meta_description', 
			'short_description',
			'long_description'
			
			
			
			)

		labels = {
			'title': "Name",
			'slug' : "URL",
			'meta_title' : "SEO-Titel",
			'meta_description' : "SEO-Beschrieb",
			'sort' : "Sortierung",
			'short_description': "Kurzbeschrieb",
			'long_description' : "Produktbeschrieb",
			'thumbnail' : "Bild",
			'thumbnail_alt' : "Bildbeschrieb",

			
		}

		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
			'slug': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

			'sort': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
			
			
			'meta_title': forms.TextInput(attrs={
				'class': 'form-control',
				}),
			'meta_description': forms.TextInput(attrs={
				'class': 'form-control',
				}),


			'thumbnail_alt': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
			

			'short_description': forms.Textarea(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

			
		}



class ServiceForm(forms.ModelForm):


	class Meta:
		model = Service
		fields = (
			'sort',
			'name',

			'short_description'
			
			)

		labels = {
			'name': "Name",
			'short_description': "Beschrieb",
			'thumbnail' : "Bild",
			'thumbnail_alt' : "Bildbeschrieb",
			'sort' : "Sortierung",

			
		}

		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

			'sort': forms.NumberInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
			'thumbnail_alt': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

			'short_description': forms.Textarea(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
	
		}


class ModuleTextForm(forms.ModelForm):
	class Meta:
		model = TextModul
		fields = (
			
			'name',
			'text',
			'text_foreign'

			)

		widgets = {

		'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

		'text': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),

		'text_foreign': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
		}

class ModuleImageForm(forms.ModelForm):
	class Meta:
		model = ImageModul
		fields = (
			
			'__all__'

			)

		widgets = {

		'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
		}

class ModuleImageTextForm(forms.ModelForm):
	class Meta:
		model = TextImageModul
		fields = (
			
			'__all__'

			)

		widgets = {

		'name': forms.TextInput(attrs={
				'class': 'form-control',
				'required': 'true'
				}),
		}



class FileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = (
			
			'__all__'

			)
		labels = {

		'name': "name",
		'alt': "alt",
		'file': "Datei",

						
		}

		widgets = {

		'name': forms.TextInput(attrs={
				'class': 'form-control',
				}),
	
			'file' : forms.FileInput(attrs={
				'class': 'form-control',
				}),
			'alt': forms.TextInput(attrs={
				'class': 'form-control',
				}),

		}


class PartnerForm(forms.ModelForm):
	class Meta:
		model = Partner
		fields = (
			
			'__all__'

			)
		labels = {

		'name': "Name",
		'short_name': "Kurzname",
		'image': "Bild",
		'image_alt': "Bildbeschrieb",
		"sort": "Sortierung",
		"description" : "Beschreibung-Partnerschaft"

						
		}

		widgets = {

		'name': forms.TextInput(attrs={
				'class': 'form-control',
				}),
		'short_name': forms.TextInput(attrs={
				'class': 'form-control',
				}),
		'sort': forms.NumberInput(attrs={
				'class': 'form-control',
				}),
		'description': forms.TextInput(attrs={
				'class': 'form-control',
				}),
	
	

		}

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = (
			'title',
			'description'
			)
		labels = {
		'title': "Titel",
						
		}

		widgets = {

		'title': forms.TextInput(attrs={
				'class': 'form-control',
				}),
		}


class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = (
			
			'image',
			'alt'

			)
		labels = {

		'image': "image",
		'alt': "alt",
						
		}

		widgets = {
	
			'image' : forms.FileInput(attrs={
				'class': 'form-control',
				}),
			'alt': forms.TextInput(attrs={
				'class': 'form-control',
				}),
		}

class ServiceGalleryForm(forms.ModelForm):
	class Meta:
		model = ServiceGallery
		fields = (
			
			'image',
			'alt'

			)
		labels = {

		'image': "image",
		'alt': "alt",
						
		}

		widgets = {
	
			'image' : forms.FileInput(attrs={
				'class': 'form-control',
				}),
			'alt': forms.TextInput(attrs={
				'class': 'form-control',
				}),
		}

class BlogGalleryForm(forms.ModelForm):
	class Meta:
		model = BlogGallery
		fields = (
			'image',
			'alt'
			)
		labels = {
		'image': "image",
		'alt': "alt",
						
		}
		widgets = {
	
			'image' : forms.FileInput(attrs={
				'class': 'form-control',
				}),
			'alt': forms.TextInput(attrs={
				'class': 'form-control',
				}),
		}

class RegistrationForm(SignupForm):
	username = forms.CharField(max_length=500, required=True, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Benutzername',
						'class': 'form-control',
						}),
					help_text='Bitte einen gültigen Benutzernamen eingeben'
					)

	first_name = forms.CharField(max_length=500, required=True, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Vorname',
						'class': 'form-control',
						}),
					help_text='Bitte einen gültigen Vornamen eingeben')

	last_name = forms.CharField(max_length=500, required=True, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Nachname',
						'class': 'form-control',
						}),
					help_text='Bitte einen gültigen Nachnamen eingeben')

	email = forms.EmailField(max_length=500, required=True, label="",
					widget=forms.EmailInput(attrs={
						'placeholder': 'E-Mail Adresse',
						'required': True, 
						'class': 'form-control',
						'type': 'email'
						}),
					help_text='Bitte eine gültige E-Mail Adresse eingeben')

	firmenname = forms.CharField(max_length=500, required=False, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Firmenname',
						'class': 'form-control'

						}))

	strasse = forms.CharField(max_length=500, required=True, label="Adresse",
					widget=forms.TextInput(attrs={
						'placeholder': 'Strasse',
						'class': 'form-control'

						}),
					help_text='Bitte eine gültige Strasse eingeben')

	nr = forms.CharField(max_length=500, required=True, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Nr.',
						'class': 'form-control'

						}),
					help_text='Bitte eine gültige Strassen-Nr. eingeben')

	plz = forms.CharField(max_length=500, required=True, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'PLZ',
						'class': 'form-control'

						}))

	ort = forms.CharField(max_length=500, required=True, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Ort',
						'class': 'form-control'

						}),
					help_text='Bitte einen gültigen Ort eingeben')

	phone = forms.CharField(max_length=500, required=True, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Telefon-Nr.',
						'class': 'form-control'

						}),
					help_text='Bitte eine gültige Telefon-Nr. eingeben')

	mobile = forms.CharField(max_length=500, required=False, label="",
					widget=forms.TextInput(attrs={
						'placeholder': 'Mobile-Nr.',
						'class': 'form-control'

						}))

	land = CountryField().formfield(
					widget=forms.Select(attrs={
						'class': 'form-control'

						}),
					help_text='Bitte ein gültiges Land auswählen')
	newsletter = forms.BooleanField(required=False)

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['email'].label = ""
		self.fields['password1'].label = "Passwort:"
		self.fields['password2'].label = "Passwort (wiederholen):"
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Passwort'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Passwort wiederholen'})
		

	def signup(self, request, user):
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		user.password1 = self.cleaned_data['password1']
		user.password2 = self.cleaned_data['password2']
		user.save()
		return user

	def save(self, request):
		user = super(RegistrationForm, self).save(request)
		kunde, created = Kunde.objects.get_or_create(user=user)
		kunde.firmenname = self.cleaned_data['firmenname']
		kunde.newsletter = self.cleaned_data['newsletter']
		kunde.phone = self.cleaned_data['phone']
		kunde.mobile = self.cleaned_data['mobile']
		kunde.rabatt = 0
		kunde.save()
		address, created = Address.objects.get_or_create(user=user)
		address.user.first_name = self.cleaned_data['first_name']
		address.user.last_name = self.cleaned_data['last_name']
		address.rechnung_strasse = self.cleaned_data['strasse']
		address.rechnung_nr = self.cleaned_data['nr']
		address.rechnung_ort = self.cleaned_data['ort']
		address.rechnung_land = self.cleaned_data['land']
		address.rechnung_plz = self.cleaned_data['plz']
		address.address_type = "B"
		address.save()
		return user
