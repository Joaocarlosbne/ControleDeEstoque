from django.contrib import admin
from django.urls import path
from proj2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adicionar/', views.add_produto, name='add_produto'),
    path('editar/<int:id>/', views.edit_produto, name='edit_produto'),
    path('remover/<int:id>/', views.delete_produto, name='delete_produto'),
]