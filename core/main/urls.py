from django.urls import path
from .views import HomeListView,Homedetail,aboutus,HomeSlide,HomeProduct
from . import views


urlpatterns =[
  path('',HomeListView.as_view(), name = 'home'),
  path('blog/<int:id>',Homedetail.as_view(), name = 'blog'),
]