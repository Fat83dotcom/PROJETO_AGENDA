from django.urls import path, include
from . import views

urlpatterns = [
    path('', include(views.login, name='index-login')),
    path('login/', include(views.login, name='login')),
    path('logout/', include(views.logout, name='logout')),
    path('cadastro/', include(views.cadastro, name='cadastro')),
    path('dashboard/', include(views.dashboard, name='dashboard')),
]
