from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("shop", views.shop, name="shop"),
    path("login", views.login_1, name="login"),
    path("register", views.register_1, name="register"),
     path('product_details/<int:id>',views.product_details, name="product_details"),
]