
from django.urls import path
from .views import vue_test


urlpatterns = [
  path('', vue_test, name='index'),
]