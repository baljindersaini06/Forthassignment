from django.urls import path
from django.conf.urls import url
from . import views 
#from .views import ShowClient

urlpatterns=[
    path('showclient',views.sort, name='showclient'),
    path('addclient', views.create_client, name='addclient'),
    path('updateclient/<int:pk>',views.client_update, name='updateclient'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search_results'),
    path('clientdelete/<int:pk>', views.delete, name='client_delete'),
    #path('showclient',ShowClient.as_view(), name='showclient'),
]