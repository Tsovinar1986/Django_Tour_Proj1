from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

# Create your models here.

      
    
class HomeSlide(models.Model):
    slide = models.CharField('slide name', max_length=100)
    about = models.CharField('slide about',max_length=1000)
    img = models.ImageField('slide image', upload_to ='media')
    
    
    def __str__(self):
            return self.slide
         
    # def get_absolute_url(self):
    #     return reverse('home')

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'

class TourIdea(models.Model):
    name = models.CharField('Tour idea name',max_length=30, blank=True)
    describe = models.TextField('Tour idea about', max_length=500, blank=True)
    img = models.ImageField('Tour idea image',upload_to ='media',blank=True)
    in_page = models.BooleanField(blank=True)
    price = models.IntegerField('Tour idea price', default=5000,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tour Idea'
        verbose_name_plural = 'Tour Ideas'
        
class Homeaboutus(models.Model):
    title = models.CharField('homeaboutus page title', max_length=100, blank=True)
    img = models.ImageField('Image of the compas on home page', upload_to ='media',blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Title'
    
class HomeProduct(models.Model):
        name = models.CharField('Product name', max_length=500, blank = True)
        decsribe = models.TextField('Product describtion', blank = True)
        price = models.IntegerField('Product price', blank = True) 
        img = models.ImageField('Product image', upload_to ='media', blank =True)   
        
        def __str__(self):
           return self.name
    
        class Meta:
              verbose_name = 'Home Product'
              verbose_name_plural = 'Home Products'
              
class HomeStaysType(models.Model):
    name = models.CharField('Home stay type name', max_length=50,blank=True)
    describe = models.TextField('Home stay type describtion', max_length=50,blank=True)
    img = models.ImageField('Home stays type images',upload_to='media',blank=True)
    price = models.IntegerField('Home stay prices', default=0,blank=True)
    in_page = models.BooleanField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Home stay Type'
        verbose_name_plural = 'Home stay Types'
        
class HomeServices(models.Model):
    types = models.FileField('Home services types', max_length=30, blank=True)
    img = models.ImageField('Home services images', upload_to = 'media', blank =True)
    
    def __str__(self):
        return self.types
    
    class Meta:
        verbose_name = 'Home services type'
        verbose_name_plural = 'Home services types'
        
class NextTourPlace(models.Model):
    name = models.CharField('Next tour place name', max_length=100,blank=True)
    describe = models.TextField('Next tour place describtion', max_length=500, blank=True)
    img = models.ImageField('Next tour place image', upload_to ='media', blank=True)
    price = models.IntegerField('Next tour place price',blank=True)
    in_page = models.BooleanField()
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Next tour place'
        verbose_name_plural = 'Next tour places'
        
class SubscribeNow(models.Model):
    e_mail = models.EmailField('e- mail of the subscriber', max_length=100,blank=True)
        
                        
class flights(models.Model):
    flights_from =models.CharField('Flight from where the travelers comes', max_length=100,blank = True)
    flights_to =models.CharField('Flight to where they go', max_length=100,blank = True)
    img = models.ImageField('Flight image',upload_to ='media',blank = True)
    price =models.IntegerField('Price of the flight',blank = True)
    
    def __str__(self):
        return self.flights_from, self.flights_to
    
    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural ='Flights'   
        
class aboutus(models.Model):
    name = models.CharField('About page name',max_length=3000,blank=True)
    about = models.TextField('about our company what we giva and what we have',blank = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about our traveling types'        

class blog(models.Model):
    name = models.CharField('About page name',max_length=3000,blank=True)
    about = models.TextField('The describtion of the travel place on the pages in blog part',blank=True)
    img = models.ImageField('the travel place picture', upload_to = 'media',blank = True)
    price = models.IntegerField('Travel price', null=True)
    
    def __str__(self):
        return self.name,self.about
    
    class Meta:
        verbose_name = 'travel place name'
        verbose_name_plural = 'travel places names'
        
class stays(models.Model):
    neighborhood = models.CharField('Place neighborhood', max_length=50,blank = True)
    city = models.CharField('Place city', max_length=50, blank = True)
    min_price = models.CharField('Price which will be for the staying place minimum how much',max_length=50,blank = True)
    max_price = models.CharField('Price which will be for the staying place maximum how much',max_length=50,blank = True)
    property_status = models.CharField('Property status what will be', max_length=50,blank = True)
    property_type  = models.CharField('Property type what will be',max_length=50, blank = True)
    BHK = models.CharField('BHK',max_length=50, blank = True)
    aminities = models.CharField('what we want to have in our hotel or hostel',max_length=50,blank = True)
    bedroom = models.CharField('How much bedrooms', max_length=50,blank = True)
    bathroom = models.CharField('How many bathrooms',max_length=50,blank = True)
    
    def __str__(self):
        return self.neighborhood, self.city,self.min_price,self.max_price,self.aminities,self.bathroom,self.bedroom,self.BHK,self.property_status,self.property_type
    
    class Meta:
        verbose_name = 'Stay'
        verbose_name_plural = 'Stays'
        
class Cart(models.Model):
    name = models.CharField('Cart name', max_length=100,blank=True)
    numbers = models.IntegerField('Cart numbers',blank=True)
    user = models.CharField('User name', max_length=100,blank=True)

    def __str__(self):
        return self.name,self.user

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

class UserCarts(models.Model):
    name = models.CharField('User name', max_length=30,blank=True)
    cart_number = models.IntegerField('Cart number',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


    
       