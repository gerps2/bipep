from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paciente/', include('paciente.urls')),
    path('equipe/', include('equipe.urls')),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]