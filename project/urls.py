from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('traker_app.urls')),  # This includes all URLs defined in traker_app
]
