from django.urls import path

# da pasta que estou, import views
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
