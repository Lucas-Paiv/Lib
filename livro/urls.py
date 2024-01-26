from django.urls import path
from . import views #importando a pasta livro

urlpatterns = [

    path('home/', views.home, name='home'),
    path('ver_livro/<int:id>', views.ver_livros, name='ver_livros')

]
