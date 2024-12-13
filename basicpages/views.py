from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from products.models import Product
from django.http import HttpResponse
from products.models import Product, Comments, Category, SubCategory
from django.contrib.auth.models import User

def home_page(request):
    products = Product.objects.prefetch_related('product_images').all()

    # print(products[0].image.url)
    for product in products:
        print(product.name)
        for image in product.product_images.all():
            print(image.image.url)  # Access the image URL
            
    context={'page':"Home", 'products':products}
    return render(request, 'pages/home/home.html', context)

def single_product(request, slug):
    product = Product.objects.prefetch_related('product_rating').filter(slug=slug)
    comments=Comments.objects.filter(product=product[0])
    context={'product':product[0], "comments": comments}
    return render(request, 'pages/products/singleProduct.html', context)

def add_comment(request, id, slug):
    try:
        if request.method=="POST":
            data=request.POST
            comment=Comments.objects.create(product_id=id, user=request.user, comment=data  ['comment'])
            return redirect(f'/product/{slug}/')
    except Exception as e:
        print("Error", e)
        return HttpResponse("Error occured")
    

def delete_comment(request, id, slug):
    try:
        comment=Comments.objects.filter(id=id)
        if(comment.exists()):
            comment.delete()
            
        return redirect(f'/product/{slug}/')
    except Exception as e:
        print(e)
    

def category_products(request, slug):
    try:
        category=Category.objects.filter(slug=slug)
        category=category[0]
        products=Product.objects.prefetch_related('product_images').filter(category=category)
        print(products)
        context={'products':products, 'category':category.name, 'page_type':'category'}
        return render(request,'pages/products/category.html', context)
    except Exception as e:
        print(e)
        return HttpResponse("Error occured")
    
def sub_category_products(request, slug):
    try:
        sub_category=SubCategory.objects.filter(slug=slug)
        sub_category=sub_category[0]
        products=Product.objects.prefetch_related('product_images').filter(sub_category=sub_category)
        print(products)
        context={'products':products, 'sub_category':sub_category.sub_category_name, 'page_type':'sub_category'}
        return render(request,'pages/products/category.html', context)
    except Exception as e:
        print(e)
        return HttpResponse("Error occured")
        