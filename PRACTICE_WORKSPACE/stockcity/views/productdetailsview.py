from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from stockcity.models import Product

class ProductDetailsView(TemplateView):
    template_name = "stockcity/productdetails.html"
    def get(self,request,id): #id is used for hyper link purpose. and get function is used to return the html
        product = Product.objects.get(id=id) #based on the id get the product details.
        context = {
            "title":product.Title, #use the info in productdetails.html as title.
            "Date":product.Date,
            "Description":product.Description
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context,request))