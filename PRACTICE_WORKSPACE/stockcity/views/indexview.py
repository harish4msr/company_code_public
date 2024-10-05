from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader  #To consider the data from index.html to return in website. we need to import loader.
from stockcity.models import Product  #import the Products from the data base.

class IndexView(TemplateView): #The class name should be same as the file name indexview.py.
    template_name = "stockcity/index.html"  #To consider the data from index.html to return in website.
    def get(self,request):
        products = Product.objects.order_by("Title")  #get the product details and store in product variable.
        context = {
            "title": "Stock Split and Bonus Newssss",
            "products": [{"id": p.id, "Title": p.Title, "Date": p.Date} for p in products]}  #consider the data from the database, dont hardcode ,"id":p.id is added in order to crete the hyper link.
        template = loader.get_template(self.template_name) #consider the data from index.html to return in website.
        return HttpResponse(template.render(context,request)) #consider the data from index.html to return in website.