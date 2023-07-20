from django.urls import path
from eccomerceapp import views

app_name = "app_name"

urlpatterns = [
    path('',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('signup',views.signup,name="signup"),
    path('login',views.log_in,name="login"),
    path('contact',views.contact,name="contact"),
    path('logout',views.log_out,name="logout"),
    path('category',views.menu,name="category"),
    path('product=<int:id>',views.product,name="product"),
]

