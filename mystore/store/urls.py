from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    # path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # # path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]
