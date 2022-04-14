from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name = 'projects'),
    path('create-project/', views.create, name = 'create'),
    path('create-project/add-project/', views.add, name = 'add')
]