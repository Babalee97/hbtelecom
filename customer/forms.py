#from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Subscribers

class SubscribersUserCreationForm(UserCreationForm):
	class Meta:
		model = Subscribers
		fields = ['username', 'email']

class SubscribersUserChangeForm(UserChangeForm):
	class Meta:
		model = Subscribers
		fields = ['username', 'email']

class SubscriberForm(forms.ModelForm):
        class Meta:
        	model = Subscribers
        	fields = ['username', 'password', 'phone_number', "first_name", "last_name"]
        
#class SubUsersForm(forms.ModelForm):
        	#class Meta:
        		#model = SubUsers
        	#	fields = ['phone_number']
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        