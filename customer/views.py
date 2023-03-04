from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import SubscriberForm
from .models import Subscribers

class SubscriberFormView(View):
    form_class1 = SubscriberForm
    template_name = 'customer/registration_form.html'

    def get(self, request):
        form1= self.form_class1(None)
        return render(request, self.template_name,
        {'base':form1})

    def post(self, request):
        form1 = self.form_class1(request.POST)
 
        if form1.is_valid():
            user = form1.save(commit=False)
            	
            username = form1.cleaned_data['username']
            password = form1.cleaned_data['password']
            	
            user.username = username
            user.set_password(password)
            user.save()
        return render(request, self.template_name, {'base':form1})
            

def fetch_user(request, phone):
            data = Subscribers.objects.all()
            user = data.get(phone_number=phone)
            return HttpResponse(request, user)
            

def add_to_balance(request, phone, fund):
            user = fetch_user(request, phone)
            initial = user.balance
            new = initial + fund
            user.balance = new
            user.save()
            
def deduct_from_balance(request, phone, topup):
            user = fetch_user(request, phone)
            initial = user.balance
            new = initial - topup
            user.balance = new
            user.save()
            
def fetch_balance(request, phone):
            user = fetch_user(request, phone)
            balance = user.balance 
            return balance
            
            
            
            
           
      
