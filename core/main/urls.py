from django.urls import path
from .views import HomeView,HomeDetailView,aboutus
from . import views


urlpatterns =[
  path('',HomeView.as_view(), name = 'home'),
  path('blog/<int:id>',HomeDetailView.as_view(), name = 'blog'),  
  path('aboutus/',views.aboutus, name = 'aboutus'),
]