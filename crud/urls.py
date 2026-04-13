from django.urls import path
from crud import views

urlpatterns=[
    path("",views.home, name='home'),
    path("edit/<int:id>/",views.edit, name='edit'),
    path("delete/<int:id>/",views.delete, name='delete'),
]
