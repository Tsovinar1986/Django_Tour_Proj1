from django.urls import path
from . import views
from .views import HomeView,HomeDetailView

urlpatterns =[
  path('', HomeView.as_view(),  name = 'home'), 
  path('<int:id>',HomeDetailView.as_view(), name = 'blog'),
  path('aboutus/',views.aboutus, name = 'aboutus'),
  path('stays/',views.stays, name = 'stays'),
  path('flights/',views.flights, name = 'flights')
]
