from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('films.urls')),  # Делает 'films' приложением по умолчанию для корневого URL
]
