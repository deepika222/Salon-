from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("serve/", views.serve, name="serve"),
    path("price/", views.price, name="price"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path("prac/", views.prac, name="prac"),
    path("pp/", views.pp, name="pp")
]
