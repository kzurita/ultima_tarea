from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('crear/', views.crear_evento, name='crear_evento'),
    path('inscribirse/<int:evento_id>/', views.inscribirse_evento, name='inscribirse_evento'),
    path('signup/', views.signup, name='signup'),
]
