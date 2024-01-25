from django.urls import path
from . import views #importando a pasta livro

urlpatterns = [

    path('home/', views.home, name='home')

]
