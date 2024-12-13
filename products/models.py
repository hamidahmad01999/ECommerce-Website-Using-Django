from django.db import models
from base.models import *
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Category(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="categories", null=True, blank=True)
    
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Category ,self).save(*args , **kwargs)
    
    def __str__(self) -> str:
        return self.name
    

class SubCategory(BaseModel):
    mainCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="sub_category")
    sub_category_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="subcategory", blank=True, null=True)
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.sub_category_name)
        super(SubCategory ,self).save(*args , **kwargs)
        
    def __str__(self) -> str:
        return self.sub_category_name
    

    
class ColorVarient(BaseModel):
    color = models.CharField(max_length=20)
    extra_price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.color
    
class SizeVarient(BaseModel):
    size = models.CharField(max_length=20)
    extra_price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="subcategory")
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=5000,default="" ,null=True)
    price = models.IntegerField(null=False, blank=False)
    discount = models.IntegerField(null=True, blank=True, default=0)
    total_products = models.IntegerField(null=False, blank=False, default=0)
    sold_products = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    total_ratings = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True, null=True)
    size_varient = models.ManyToManyField(SizeVarient, blank=True)
    color_varient = models.ManyToManyField(ColorVarient, blank=True)
    is_active = models.BooleanField(default=True)
    
    
    def save(self, *args, **kwargs):
        related= SubCategory.objects.filter(sub_category_name=self.sub_category)
        if(related[0].mainCategory!=self.category):
            raise ValidationError("Selected wrong Category and subcategory field")
        else:
            self.slug = slugify(self.name)
            super(Product, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
    def get_first_image(self):
        return self.product_images.first()
    
    def get_comments(self):
        comments = Comments.objects.filter(product=self)
        print("Check model comments", comments)
        return comments
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="products")
    
class Comments(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updateed_at = models.DateField(auto_now=True)
    comment = models.TextField(max_length=500)
    
    def is_user_image(self):
        print("Profile image",self.user.profile.image)
        return self.user.profile.image != ''
    
    def get_user_image(self):
        print("User image: ",self.user.profile.image.url)
        return self.user.profile.image.url
    
    def __str__(self) -> str:
        return f"{self.user} - {self.product}"

class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rating")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_rating")
    rating = models.IntegerField(null=False, blank=False)
    
