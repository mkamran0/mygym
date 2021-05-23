from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact


# Create your views here.
def index(request):
    return render(request,'index.html')
    
def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def joining(request):
    return render(request,'join.html')

def joinsuccess(request):
    cn = request.POST.get('cname', 'default')
    cmobile = request.POST.get('mobile', 'default')
    cage = request.POST.get('age', 'default')
    ccity = request.POST.get('city', 'default')
    cstate = request.POST.get('state', 'default')
    ccountry = request.POST.get('country', 'default')
    cgender = request.POST.get('gender', 'default')
    ccategory = request.POST.get('category', 'default')
    myregistration = Contact(name=cn, mobile=cmobile, age=cage, city=ccity, state=cstate, country=ccountry, gender=cgender, category=ccategory)
    myregistration.save()
    return render(request, 'joinsuccess.html')
    
def calling(request):
    return render(request, 'call.html')

def messaging(request):
    return render(request, 'message.html')

def fees_details(request):
    return render(request, 'fees.html')

def trainer(request):
    return render(request, 'trainers.html')

def yogabest(request):
    return render(request, 'yoga.html')

def yogatrainer(request):
    return render(request, 'yoga_trainers.html')

def dietplans(request):
    return render(request, 'dplans.html')

def dietplanners(request):
    return render(request, 'dplanners.html')

def viewdetails1(request):
     return render(request, 'view1.html')

def viewdetails2(request):
     return render(request, 'view2.html')

def viewdetails3(request):
    return render(request, 'view3.html')




    
    
    
    # cn = request.POST.get('cname', 'default')
    # cmobile = request.POST.get('mobile', 'default')
    # cage = request.POST.get('age', 'default')
    # print(cn)
    # print(cmobile)
    # print(cage)
    # return HttpResponse("done")




    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('join') 
    # else:
    #     form = RegistrationForm()
    # context = {'c_form':form}
    # return render(request,'join.html',context)

