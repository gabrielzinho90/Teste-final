from django.contrib import admin
from django.urls import path
from .views import calculate_savings, calculator


urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/', calculate_savings, name='calculate_savings'),
    path('', calculator, name='calculator'),  # Adicione esta linha para a URL raiz
]