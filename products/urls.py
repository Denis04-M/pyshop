from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='galaxy hotel'),
   path('cart/', views.cart, name='cart'),
   path('shipping/', views.shipping, name='shipping'),
   path('beverages/', views.beverages, name='beverages'),
   path('vegetables/', views.vegetables, name='vegetables'),
   path('meat products/', views.meat, name='meat'),
   path('meals/', views.meals, name='meals'),
   path('update_item/', views.updateItem, name='update_item'),
   path('process_order/', views.processOrder, name='process_order'),
   path('orders_placed/', views.placeOrder, name='orders_placed'),
   path('report/', views.report, name='report'),
   path('chart/', views.chart, name='chart')
]
