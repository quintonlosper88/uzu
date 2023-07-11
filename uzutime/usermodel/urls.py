from django.urls import path
from .views import homeView,userscannedView

urlpatterns = [
    path("",homeView,name="home"),
    path("user/",userscannedView,name="userscanned")
]