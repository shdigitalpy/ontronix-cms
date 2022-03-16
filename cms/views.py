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


@staff_member_required
def cms_gallery_images(request, pk):
	product = get_object_or_404(Product, pk=pk)

	gallery = Gallery.objects.filter(product=product)

	context = {
		'gallery': gallery,
		'product': product,
				}

	return render(request, 'cms-gallery.html', context)


@staff_member_required
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

@staff_member_required
def cms_gallery_image_delete(request, ppk, pk):
	eintrag = get_object_or_404(Gallery, pk=pk)
	eintrag.delete()
	messages.info(request, "Das Bild wurde gelöscht.")
	return redirect("cms_gallery_images", pk=ppk)



#service gallery start

@staff_member_required
def cms_service_gallery_images(request, pk):
	service = get_object_or_404(Service, pk=pk)

	gallery = ServiceGallery.objects.filter(service=service)

	context = {
		'gallery': gallery,
		'service': service,
				}

	return render(request, 'cms-service-gallery.html', context)


@staff_member_required
def cms_service_gallery_image_add(request, pk):

	service = get_object_or_404(Service, pk=pk)

	if request.method == "POST":
		form = ServiceGalleryForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form = form.save(commit=False)
			form.service = service
			form.save()
			return redirect('cms_service_gallery_images', pk=pk)

		else:
			messages.error(request, "Error")
	else: 
		form = ServiceGalleryForm(request.POST or None, request.FILES or None)

	context = {
		'form': form,
		'service': service,
				}

	return render(request, 'cms-service-gallery-add.html', context)


@staff_member_required
def cms_service_gallery_image_delete(request, ppk, pk):
	eintrag = get_object_or_404(ServiceGallery, pk=pk)
	eintrag.delete()
	messages.info(request, "Das Bild wurde gelöscht.")
	return redirect("cms_service_gallery_images", pk=ppk)


#service gallery end

#Blog
@staff_member_required
def cms_blog(request):
	
	blog = Blog.objects.all()
			

	context = {
		'blog': blog,
	 }
	return render(request, 'cms-blog.html', context)

@staff_member_required
def cms_blog_erfassen(request):
	if request.method == "POST":
		form = BlogForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()	
			return redirect('cms_blog')

		else:
			messages.error(request, "Error")

	else: 
		form = BlogForm()

	context = {
		'form': form,
				}
	return render(request, 'cms-blog-erfassen.html', context)


@staff_member_required
def cms_blog_bearbeiten(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	
	if request.method == "POST":
		form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
		if form.is_valid():
			form.save()
			return redirect('cms_blog')

		else:
			messages.error(request, "Error")
	else: 
		form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
	context = {
		'form': form,
		'blog': blog,
		
				}
	return render(request, 'cms-blog-bearbeiten.html', context)

@staff_member_required
def cms_blog_löschen(request, pk):
	eintrag = get_object_or_404(Blog, pk=pk)
	eintrag.delete()
	messages.info(request, "Der Blog wurde gelöscht.")
	return redirect("cms_blog")	

#blog gallery start

@staff_member_required
def cms_blog_gallery_images(request, pk):
	blog = get_object_or_404(Blog, pk=pk)

	gallery = BlogGallery.objects.filter(blog=blog)

	context = {
		'gallery': gallery,
		'blog': blog,
				}

	return render(request, 'cms-blog-gallery.html', context)


@staff_member_required
def cms_blog_gallery_image_add(request, pk):
	blog = get_object_or_404(Blog, pk=pk)

	if request.method == "POST":
		form = BlogGalleryForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form = form.save(commit=False)
			form.blog = blog
			form.save()
			return redirect('cms_blog_gallery_images', pk=pk)

		else:
			messages.error(request, "Error")
	else: 
		form = BlogGalleryForm(request.POST or None, request.FILES or None)

	context = {
		'form': form,
		'blog': blog,
				}

	return render(request, 'cms-blog-gallery-add.html', context)


@staff_member_required
def cms_blog_gallery_image_delete(request, ppk, pk):
	eintrag = get_object_or_404(BlogGallery, pk=pk)
	eintrag.delete()
	messages.info(request, "Das Bild wurde gelöscht.")
	return redirect("cms_blog_gallery_images", pk=ppk)

#blog gallery end

# pages and module

@staff_member_required
def cms_pages(request):
	pages = Page.objects.all()
	
	context = {
	"pages" : pages,
	}
	return render(request, 'cms-pages.html', context)

@staff_member_required
def cms_section_detail(request, pk):
	section = get_object_or_404(Section, pk=pk)

	context = {
	"section" : section,
	}
	return render(request, 'cms-section-details.html', context)

@staff_member_required
def cms_module_detail(request, pk, module, section_pk):

	if module == 'text_module':
		module_final = get_object_or_404(TextModul, pk=pk)

	elif module == 'image_module': 
		module_final = get_object_or_404(ImageModul, pk=pk)

	elif module == 'text_image_module': 
		module_final = get_object_or_404(TextImageModul, pk=pk)

	else:
		print('Error')

	context = {
	"module_final" : module_final,
	'section_pk' : section_pk,
	'module' : module,
	}
	return render(request, 'cms-module-detail.html', context)

@login_required
def cms_module_bearbeiten(request, pk, module, section_pk):
	
	if module == 'text_module':
		module_final = get_object_or_404(TextModul, pk=pk)

	elif module == 'image_module': 
		module_final = get_object_or_404(ImageModul, pk=pk)

	elif module == 'text_image_module': 
		module_final = get_object_or_404(TextImageModul, pk=pk)

	else:
		print('error')
	
	if request.method == "POST":
		if module == 'text_module':
			form = ModuleTextForm(request.POST or None, request.FILES or None, instance=module_final)

		elif module == 'image_module': 
			form = ModuleImageForm(request.POST or None, request.FILES or None, instance=module_final)

		elif module == 'text_image_module': 
			form = ModuleImageTextForm(request.POST or None, request.FILES or None, instance=module_final)

		else:
			print('error')
		if form.is_valid():
				form.save()					
				return redirect('cms_module_detail', pk=pk, module=module, section_pk=section_pk)

		else:
			messages.error(request, "Error")
	else: 
		if module == 'text_module':
			form = ModuleTextForm(request.POST or None, request.FILES or None, instance=module_final)

		elif module == 'image_module': 
			form = ModuleImageForm(request.POST or None, request.FILES or None, instance=module_final)

		elif module == 'text_image_module': 
			form = ModuleImageTextForm(request.POST or None, request.FILES or None, instance=module_final)

		else:
			print('error')


	context = {
		'form': form,
		'module': module,
		'section_pk': section_pk,
		'pk' : pk,
		
				}
	return render(request, 'cms-module-bearbeiten.html', context)


#partner

@staff_member_required
def cms_partner(request):
	partner = Partner.objects.all().order_by('sort')
	
	context = {
	"partner" : partner,
	}
	return render(request, 'cms-partner.html', context)

@staff_member_required
def cms_partner_erfassen(request):
	if request.method == "POST":
		form = PartnerForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()	
			return redirect('cms_partner')

		else:
			messages.error(request, "Error")

	else: 
		form = PartnerForm()

	context = {
		'form': form,
				}
	return render(request, 'cms-partner-erfassen.html', context)


@staff_member_required
def cms_partner_bearbeiten(request, pk):
	partner = get_object_or_404(Partner, pk=pk)
	
	if request.method == "POST":
		form = PartnerForm(request.POST or None, request.FILES or None, instance=partner)
		if form.is_valid():
			form.save()
			return redirect('cms_partner')

		else:
			messages.error(request, "Error")
	else: 
		form = PartnerForm(request.POST or None, request.FILES or None, instance=partner)
	context = {
		'form': form,
		'partner': partner,
		
				}
	return render(request, 'cms-partner-bearbeiten.html', context)

@staff_member_required
def cms_partner_löschen(request, pk):
	eintrag = get_object_or_404(Partner, pk=pk)
	eintrag.delete()
	messages.info(request, "Der Partner wurde gelöscht.")
	return redirect("cms_partner")	



#karriere

@staff_member_required
def cms_jobs(request):
	jobs = Job.objects.all()
	
	context = {
	"jobs" : jobs,
	}
	return render(request, 'cms-jobs.html', context)


@staff_member_required
def cms_jobs_erfassen(request):
	if request.method == "POST":
		form = JobForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()	
			return redirect('cms_jobs')

		else:
			messages.error(request, "Error")

	else: 
		form = JobForm()

	context = {
		'form': form,
				}
	return render(request, 'cms-jobs-erfassen.html', context)


@staff_member_required
def cms_jobs_bearbeiten(request, pk):
	job = get_object_or_404(Job, pk=pk)
	
	if request.method == "POST":
		form = JobForm(request.POST or None, request.FILES or None, instance=job)
		if form.is_valid():
			form.save()
			return redirect('cms_jobs')

		else:
			messages.error(request, "Error")
	else: 
		form = JobForm(request.POST or None, request.FILES or None, instance=job)
	context = {
		'form': form,
		'job': job,
		
				}
	return render(request, 'cms-jobs-bearbeiten.html', context)



@staff_member_required
def cms_jobs_löschen(request, pk):
	eintrag = get_object_or_404(Job, pk=pk)
	eintrag.delete()
	messages.info(request, "Job wurde gelöscht.")
	return redirect("cms_jobs")	

