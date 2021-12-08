from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('save/',views.savestud,name='save'),
    path('list/',views.studlist,name="list"),
    path('edit/<int:sid>',views.edit,name='edit'),
    path('update/<int:sid>',views.update,name='update'),
    path('delete/<int:sid>',views.delete,name='delete'),


]
   