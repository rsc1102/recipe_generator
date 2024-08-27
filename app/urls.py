from django.urls import path

from . import views

urlpatterns = [
    path("generate_recipes",views.generate_recipes,name='generate_recipes'),
    path("", views.index, name="index"),
]