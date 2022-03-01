'''from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.recipe, name='recipe'),
]'''


from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipe_index, name='recipe_index'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
]
