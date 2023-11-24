from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('package',views.package,name='package'),
    path('colleges/',views.colleges,name='colleges'),
]