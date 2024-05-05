from django.urls import path, include
from drf import views
urlpatterns = [
    path('', views.readAll, name='read'),
    path('createProduct', views.create, name='createProduct'),
    path('updateProduct', views.update, name='updateProduct'),
    path('deleteProduct', views.delete, name='deleteProduct'),
]