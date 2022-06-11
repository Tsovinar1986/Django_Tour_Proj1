from django.urls import path
from .views import HomeListView,Homedetail,aboutus
from . import views


urlpatterns =[
  path('',HomeListView.as_view(), name = 'home'),
  path('blog<int:id>',Homedetail.as_view(), name = 'blog'),
  path('aboutus/',views.aboutus, name ='aboutus'),
  path('stays/',views.stays,name ='stays'),
  path('flights/',views.flights, name = 'flights'),
  path('register/',views.register_request, name = 'register'),
  path('login/',views.login_request, name = 'login'),
  path('logout/',views.logout_request, name = 'logout'),
#   path('userpage', UserPageListView.as_view(), name='userpage'),
#   path('add_post/', add_post, name='add_post'),
#   path('post_detail/', post_detail, name='post_detail'),
]