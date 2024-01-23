from django.urls import path
from . import views #importando a pasta livro

urlpatterns = [

    path('cadastrar/', views.cadastrar)

]
