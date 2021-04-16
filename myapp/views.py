from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from . models import Contact,Products,Dealership,glay_gallery
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    glaynepal_gallery=glay_gallery.objects.all()
    context_gallery={
        'glaynepal_gallery':glaynepal_gallery
    }
    return render(request,'myapp/home.html',context_gallery)

def about(request):
    return render(request,'myapp/about.html')

def service(request):
    return render(request,'myapp/service.html')

def product(request):
    all_post= Products.objects.all()
    all_post=all_post
    context={"all_post":all_post}
    return render(request,'myapp/product.html',context)

def contact(request):
    if request.method == 'POST':
        name=request.POST['user_name']
        email=request.POST['email']
        address=request.POST['thau']
        message=request.POST['chitthi']
        if len(name)>3 and len(email)>3 and len(address)>3 and len(message)>3:
            messages.success(request,"Your form has been submited.")
            contact_details=Contact(name=name,email=email,address=address,message=message)
            contact_details.save()
        else:
            messages.error(request,'Please!!fill your form correctly')
    return render(request,'myapp/contact.html')

def apply_form(request):
    if request.method == 'POST':
        name=request.POST['company_name']
        registeration_number=request.POST['reg_num']
        email=request.POST['Email_id']
        number=request.POST['mobile']
        address=request.POST['place']
        message=request.POST['patro']
        if len(name)>3 and len(email)>3 and len(number)>3 and len(registeration_number)>3 and len(address)>3 and len(message)>3:
            messages.success(request,"Your Applied Request has been submited.")
            apply_details=Dealership(name=name,registeration_number=registeration_number,email=email,number=number,address=address,message=message)
            apply_details.save()
        else:
            messages.error(request,'Please!!fill your form correctly')
    return redirect('home')


