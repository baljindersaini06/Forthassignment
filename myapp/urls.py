from django.urls import path
from django.conf.urls import url
from . import views 
from .views import clientView, SearchResultsView, edit_client, client_update, ClientDelete, ViewClient


urlpatterns=[
    path('addclient', clientView.as_view(), name='addclient'),
    path('showclient', views.show, name='showclient'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('editclient',views.edit_client, name='editclient'),
    path('updateclient/<int:pk>',views.client_update, name='updateclient'),
    path('clientdelete/<int:pk>', ClientDelete.as_view(), name="client_delete"),
    path('', views.home, name='home'),
    #path('showclient',ViewClient.as_view(), name='showclient'),
]