from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

# Aca van todas las rutas de las cuentas
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
