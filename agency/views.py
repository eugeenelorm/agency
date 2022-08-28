
from django.shortcuts import render, redirect
from . models import Contactform,Portfolio,Team

# Create your views here.
def home(request):
    if request.method == 'POST' and 'submit' in request.POST:
        name = request.POST['name']
        email= request.POST['email']
        phonenumber = request.POST['phonenumber']
        message = request.POST['message']
        contact = Contactform(name=name, email=email, phonenumber=phonenumber, message=message)
        # contact.name = name
        # contact.email=email
        # contact.phonenumber = phonenumber
        # contact.message = message
        contact.save()
        return redirect('/')

    items = Portfolio.objects.all()
    member = Team.objects.all()
  
    return render(request, 'index.html',{'items':items, 'member':member})