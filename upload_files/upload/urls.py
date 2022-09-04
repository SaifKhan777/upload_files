from django.contrib import admin
from django.urls import path 
from upload import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("",views.index,name="index"),
    path("addfile",views.addfile,name="addfile"),
    path("deletefile",views.deletefile,name="deletefile"),
     path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout")

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)