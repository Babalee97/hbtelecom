from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SubscribersUserCreationForm, SubscribersUserChangeForm
from customer.models import Subscribers

class SubscribersUserAdmin(UserAdmin):
	add_form = SubscribersUserCreationForm
	form = SubscribersUserChangeForm
	model = Subscribers
	list_display = ['username', 'email', 'phone_number', 'balance']


admin.site.register(Subscribers, SubscribersUserAdmin)
