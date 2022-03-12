from django.conf.urls import include, url
from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from rest_framework.routers import DefaultRouter 

router=DefaultRouter()
router.register('Clothes',views.Clothestable,basename='Clothes')
router.register('Books',views.Bookstable,basename='Books')
router.register('Hardware',views.Hardwaretable,basename='Hardware')


urlpatterns=[
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),

]
   
urlpatterns=urlpatterns+router.urls