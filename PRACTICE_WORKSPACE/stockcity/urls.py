from django.urls import path
from stockcity.views.indexview import IndexView #is used to create route for index.html.
from stockcity.views.productdetailsview import ProductDetailsView #import  is used to make hyper link to work, that is create route for productdetailsview.

urlpatterns = [
   path("products/<int:id>", ProductDetailsView.as_view(), name="products"), #/<int:id> is added for hyperlink to work, wrt to product.id in index.html
   path("", IndexView.as_view(), name="index"),
]