from tabnanny import verbose
from tokenize import blank_re
from django.db import models

# Create your models here.

class HomeSlide(models.Model):
    name = models.CharField('slide  name', max_length=1000)
    about = models.TextField('slide about', max_length = 2000)
    image = models.ImageField('slide  image', upload_to = 'media')

    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tour'
        verbose_name_plural = 'tours'
        
class HomeProduct(models.Model):
    name = models.CharField('Product name', max_length=500, blank = True)
    decsribe = models.TextField('Product describtion', blank = True)
    price = models.IntegerField('Product price', blank = True) 
    img = models.ImageField('Product image', upload_to ='media', blank = True)   
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'HomeProduct'
        verbose_name_plural = 'HomeProducts'
        
class stays(models.Model):
    name = models.CharField('Hotel name',max_length=50, blank = True)
    img =models.ImageField('Hotel image', upload_to = 'media',blank = True)
    price = models.IntegerField('hotel one nigth price',blank = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'
        
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
    img = models.ImageField('Images of us or travel places', upload_to = 'media',blank = True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about our traveling types'        

class blog(models.Model):
    about = models.TextField('The describtion of the travel place on the pages in blog part',blank=True)
    img = models.ImageField('the travel place picture', upload_to = 'media',blank = True)
    
    def __str__(self):
        return self.about
    
    class Meta:
        verbose_name = 'travel place about'
        verbose_name_plural = 'travel places about'
        
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
        return self.name

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


    
       