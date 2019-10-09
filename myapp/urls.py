from django.urls import path
from django.conf.urls import url
from . import views 


urlpatterns=[
    path('addclient', views.create_client, name='addclient'),
    path('showclient', views.show, name='showclient'),
    path('editclient',views.edit_client, name='editclient'),
    path('updateclient/<int:pk>',views.client_update, name='updateclient'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search_results'),
    path('clientdelete/<int:pk>', views.delete, name='client_delete'),
]