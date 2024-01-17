from django.urls import path

from .views import FirstTest


urlpatterns = [
    path('test/', FirstTest.as_view(), name='create_tickets'),
    
]