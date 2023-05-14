from . import views
from django.urls import path, include
app_name='shop'

urlpatterns = [
    path('',views.AllProductCat,name='AllProductCat'),
    path('search/',views.Searchresult,name='Searchresult'), 
    path('<slug:c_slug>/',views.AllProductCat,name='product_cat'),
    path('<slug:c_slug>/<slug:p_slug>/',views.ProductDetails,name='product_details'),


]