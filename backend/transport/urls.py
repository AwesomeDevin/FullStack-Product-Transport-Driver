from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^api/v1/transport/user/$',
        views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^api/v1/transport/user/(?P<pk>\d+)/$', views.UserViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'^api/v1/transport/order/$',
        views.OrderViewSet.as_view({'get': 'list', 'post': 'create'})),
    url(r'^api/v1/transport/order/(?P<pk>\d+)/$', views.OrderViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    url(r'^api/v1/transport/file/$', views.upload),
    
]