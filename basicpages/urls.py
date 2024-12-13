from django.urls import path
from .views import *
app_name="basicpages"
urlpatterns = [
    path("",home_page, name="home_page" ),
    path("product/<slug>/", single_product, name="single_product"),
    path("products/category/<slug>", category_products, name="category_products"),
    path("products/sub-category/<slug>", sub_category_products, name="sub_category_products"),
    path("add-comment/<id>/<slug>", add_comment, name="add_comment"),
    path("delete-comment/<id>/<slug>", delete_comment, name="delete_comment")
]
