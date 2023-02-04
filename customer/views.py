from django.shortcuts import render
from django.views.generic import View
from .forms import SubscriberForm

class SubscriberFormView(View):
    form_class = SubscriberForm
    template_name = 'customer/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
 
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.username = username
            user.set_password(password)
            user.save()
            return render(request, self.template_name, {'form':form})
