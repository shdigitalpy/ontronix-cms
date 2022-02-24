from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from backend.models import *
from .forms import *
import json

@login_required
def cms(request):

	context = { }
	return render(request, 'cms.html', context)

# ------------------------------------------------Start Login / Logout

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Successfully logged in.'))
			return redirect ('cms')
		else:
			messages.success(request, ('Error - Please check your entry.'))
			return redirect ('login_user')
	else:
		context = {}
		return render(request, 'cms-login.html', context )

@login_required
def logout_user(request):
	logout(request)
	messages.success(request, ('You were successfully logged out.'))
	return redirect('login_user')
# ------------------------------------------------End Login / Logout

@staff_member_required
def cms_kunden(request):
	user1 = User.objects.all().order_by('-id')
	context = {
			'user1': user1,		
			 }
	return render(request, 'cms-kunden.html', context)

@staff_member_required
def cms_pdf(request):
	pdf = File.objects.all()
	context = {
			'pdf': pdf,
			 }
	return render(request, 'cms-pdf.html', context)

@staff_member_required
def cms_pdf_upload(request):
	if request.method == "POST":
		form = FileForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('cms_pdf')

		else:
			messages.error(request, "Error")
	else: 
		form = FileForm(request.POST or None, request.FILES or None)

	context = {
		'form': form,
				}

	return render(request, 'cms-pdf-upload.html', context)

@staff_member_required
def cms_pdf_edit(request, pk):
	file = get_object_or_404(File, pk=pk)
	
	if request.method == "POST":
		form = FileForm(request.POST or None, request.FILES or None, instance=file)
		if form.is_valid():
			form.save()
			return redirect('cms_pdf')

		else:
			messages.error(request, "Error")
	else: 
		form = FileForm(request.POST or None, request.FILES or None, instance=file)
	context = {
		'form': form,
		'file': file,
		
				}
	return render(request, 'cms-pdf-bearbeiten.html', context)

@staff_member_required
def cms_pages(request):
	pages = Page.objects.all()
	
	context = {
	"pages" : pages,
	}
	return render(request, 'cms-pages.html', context)



#Produkte

@staff_member_required
def cms_produkte(request):
	category = ' '
	filter_query = request.GET.get('category', '')
	search_query = request.GET.get('search', '')	

	if search_query:
		produkte = Product.objects.filter(Q(titel__icontains=search_query) | Q(artikelnr__icontains=search_query) | Q(kategorie__name__icontains=search_query) | Q(subkategorie__sub_name__icontains=search_query))
	
		if filter_query:
			produkte = produkte.filter(kategorie__name=filter_query)
		else:
			pass
	else:
		if filter_query:
			produkte = Product.objects.filter(kategorie__name=filter_query)
		else: 
			produkte = Product.objects.all()
			

	context = {
		'category': category,
		'produkte': produkte,
	 }
	return render(request, 'cms-produkte.html', context)



@login_required
def cms_produkte_erfassen(request):
	if request.method == "POST":
		form = ProduktForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()	
			return redirect('cms_produkte')

		else:
			messages.error(request, "Error")

	else: 
		form = ProduktForm()

	context = {
		'form': form,
				}
	return render(request, 'cms-produkte-erfassen.html', context)

@login_required
def cms_produkte_bearbeiten(request, pk):
	product = get_object_or_404(Product, pk=pk)
	
	if request.method == "POST":
		form = ProduktForm(request.POST or None, request.FILES or None, instance=product)
		if form.is_valid():
				form.save()					
				return redirect('cms_produkte')

		else:
			messages.error(request, "Error")
	else: 
		form = ProduktForm(request.POST or None, request.FILES or None, instance=product)
	context = {
		'form': form,
		'product': product,
		
				}
	return render(request, 'cms-produkte-bearbeiten.html', context)

@login_required
def cms_produkte_löschen(request, pk):
	eintrag = get_object_or_404(Product, pk=pk)
	eintrag.delete()
	messages.info(request, "Das Produkt wurde gelöscht.")
	return redirect("cms_produkte")	

#Produkte END


#Service

@staff_member_required
def cms_service(request):
	service = Service.objects.all()
			

	context = {
		'service': service,
	 }
	return render(request, 'cms-service.html', context)

@login_required
def cms_service_erfassen(request):
	if request.method == "POST":
		form = ServiceForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()	
			return redirect('cms_service')

		else:
			messages.error(request, "Error")

	else: 
		form = ServiceForm()

	context = {
		'form': form,
				}
	return render(request, 'cms-service-erfassen.html', context)

@login_required
def cms_service_bearbeiten(request, pk):
	service = get_object_or_404(Service, pk=pk)
	
	if request.method == "POST":
		form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
		if form.is_valid():
				form.save()					
				return redirect('cms_service')

		else:
			messages.error(request, "Error")
	else: 
		form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
	context = {
		'form': form,
		'service': service,
		
				}
	return render(request, 'cms-service-bearbeiten.html', context)

@login_required
def cms_service_löschen(request, pk):
	eintrag = get_object_or_404(Service, pk=pk)
	eintrag.delete()
	messages.info(request, "Die Dienstleistung wurde gelöscht.")
	return redirect("cms_service")	


#Service END


@login_required
def cms_gallery_images(request, pk):
	product = get_object_or_404(Product, pk=pk)

	gallery = Gallery.objects.filter(product=product)

	context = {
		'gallery': gallery,
		'product': product,
				}

	return render(request, 'cms-gallery.html', context)


@login_required
def cms_gallery_image_add(request, pk):

	product = get_object_or_404(Product, pk=pk)

	if request.method == "POST":
		form = GalleryForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form = form.save(commit=False)
			form.product = product
			form.save()
			return redirect('cms_gallery_images', pk=pk)

		else:
			messages.error(request, "Error")
	else: 
		form = GalleryForm(request.POST or None, request.FILES or None)

	context = {
		'form': form,
		'product': product,
				}

	return render(request, 'cms-gallery-add.html', context)

@login_required
def cms_gallery_image_delete(request, ppk, pk):
	eintrag = get_object_or_404(Gallery, pk=pk)
	eintrag.delete()
	messages.info(request, "Das Bild wurde gelöscht.")
	return redirect("cms_gallery_images", pk=ppk)


@staff_member_required
def cms_orders(request):
	order = Order.objects.filter(ordered=True)
	context = {
			'order': order,
			 }
	return render(request, 'cms-bestellungen.html', context)

