from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='homepage'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('signup/', views.signup, name='sign'),
    path('login/', views.login, name='log_user'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='update_item'),

]
