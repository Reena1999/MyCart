from django.urls import path

from . import views
from .views import userauthenticate, signupuser, loginuser, logout, search, tracker, contact, about, index, \
    productView,homepage


urlpatterns = [
    path("index/", index, name="ShopHome"),
    path("about/", about, name="AboutUs"),
    path("contact/", contact, name="ContactUs"),
    path("tracker/",tracker, name="TrackingStatus"),
    path("search/", search, name="Search"),
    path("products/<int:myid>",productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("loginuser/", loginuser, name="userlogin"),
    path("signupuser/", signupuser,name="signupuser"),
    path("user/authenticate/", userauthenticate),
    path('logout/',logout),
    path('',homepage),
]
