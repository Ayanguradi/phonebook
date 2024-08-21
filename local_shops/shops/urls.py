from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#create shop
# from .views import create_shop_view

urlpatterns = [
 
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('category/<int:category_id>/shops/', views.category_shops, name='category_shops'),
    path('category/<int:category_id>/subcategory/<int:subcategory_id>/shops/', views.subcategory_shops, name='subcategory_shops'),
    path('shop/<int:pk>/', views.shop_detail, name='shop_detail'),
    path('shop/<int:shop_id>/all-images/',views.shop_all_images, name='shop_all_images'),

    #user shop form
     path('create_shop/',views.create_shop, name='create_shop'),
      path('get_subcategories/<int:category_id>/',views.get_subcategories, name='get_subcategories'),
    #  path('api/subcategories/<int:category_id>/', views.get_subcategories, name='get_subcategories'),
     path('search/', views.search, name='search'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)