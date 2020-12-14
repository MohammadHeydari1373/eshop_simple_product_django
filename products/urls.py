from django.urls import path
from products.views import (ProductListView,
                            ProductDetailSlugView,
                            )
app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view() , name = 'product_list') ,
    path('<slug>' , ProductDetailSlugView.as_view() , name = 'productSlugDetail') ,
    # path('products-fbv/<productId>' , product_detail_view),
    # path('products-fbv' , product_list_view) ,
    # path('featured' , ProductFeaturedListView.as_view()),
    # path('featured/<pk>' , ProductDetailFeaturedView.as_view()) ,
]
