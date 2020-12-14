from django.shortcuts import render
from django.urls import reverse

from .models import Product
# Create your views here.
from django.views.generic import  ListView,DetailView
from django.http import     Http404
from django.shortcuts import get_object_or_404

#featured list

class ProductFeaturedListView(ListView) :
    template_name = 'products/product_list.html'
    def get_queryset(self):
        return reverse("products:productSlugDetail" , kwargs={"slug" : self.slug})
        #return Product.objects.get_featured()


# end featured list

#featured detail

class ProductDetailFeaturedView(DetailView ) :

    template_name = 'products/product_featured_detail.html'
    def get_queryset(self):
        return Product.objects.get_featured()


#end featured detail
class ProductDetailSlugView(DetailView ) :
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'
    def get_object(self,*args , **kwargs ):
        request = self.request
        slug =  self.kwargs.get('slug')
        try :
            product = Product.objects.get(slug = slug)
        except product.DoesNotExist :
            raise Http404("does not exist")
        except product.MultipleObjectsReturned :

            qs = Product.objects.filter(slug = slug)
            product = qs.first()
        except :
            raise Http404("page not found")
        return product






class ProductListView(ListView) :
    #queryset = get_object_or_404(Product)


    #queryset = Product.objects.all()
    template_name = 'products/product_list.html'
    # def  get_context_data(self, *args, object_list=None, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args , **kwargs)
    #     #print(context)
    #     return context
    def get_queryset(self):
        product = Product.objects.all()
        return product


def product_list_view(request) :
    object = Product.objects.all()

    context  = {
        'object' :object
    }
    return render(request , 'products/product_list.html' , context)



class ProductDetailView(DetailView ) :
    #
    # try :
    #     queryset = Product.objects.all()
    # except queryset.DoesNotExist :
    #     raise Http404('dsvn')
    #queryset = get_object_or_404(Product , id =pk)
    template_name = 'products/product_detail.html'
    def get_context_data(self,*args, object_list = None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        print(context)
        return context

    def get_object(self,*args , **kwargs ):
        request = self.request
        productId =  self.kwargs.get('pk')
        products = Product.objects.get_by_id(productId)
        if products is None :
            raise Http404("this is my costum cvb manager and is page not found")
        return products
    # def get_queryset(self , *args , **kwargs):
    #     request =self.request
    #     productId = kwargs.get('pk')
    #     product

def product_detail_view(request ,productId=None, *args , **kwargs) :
    #products = get_object_or_404(Product, id=productId)
    # try :
    #     products = Product.objects.get(id = productId)
    # except Product.DoesNotExist:
    #     raise Http404("product does not found")
    # except :
    #     print('what?')


    #products = Product.objects.get(id= productId)
    # print(args)
    # print(kwargs)
    products = Product.objects.get_by_id(productId)
    if products is None :
        raise Http404("my costum manager and this page is not found")

    context  = {
        'object' :products
    }
    return render(request , 'products/product_detail.html' , context)
