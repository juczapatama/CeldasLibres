from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import SignUpView, signup

# Aca van todas las rutas de las cuentas
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', SignUpView.as_view(), name='login'),
    path('tarifa/', SignUpView.as_view(), name='tarifa'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)