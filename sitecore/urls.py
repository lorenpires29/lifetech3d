from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('servicos/', views.servicos, name='servicos'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('orcamento/', views.orcamento, name='orcamento'),
    path('contato/', views.contato, name='contato'),
]
