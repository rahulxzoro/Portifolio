from django.shortcuts import render,redirect
from . models import Contact
# Create your views here.
def home(request):
   
    return render(request,'index.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact.objects.create(name=name, email=email, message=message)
        return redirect('home')  
    return redirect('home')  