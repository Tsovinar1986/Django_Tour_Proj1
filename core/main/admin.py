from django.contrib import admin
from .models import HomeProduct, HomeSlide,aboutus,flights,stays,User
# Register your models here.

admin.site.register(HomeSlide)
admin.site.register(HomeProduct)
admin.site.register(aboutus)
admin.site.register(flights)
admin.site.register(stays)
admin.site.register(User)




