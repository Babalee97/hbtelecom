from django.contrib import admin
from django.urls import path

from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.SubscriberFormView.as_view(), name='registration'),
]



























