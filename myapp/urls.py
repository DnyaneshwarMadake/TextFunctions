from django.urls import path
from . import views  # Ensure you're importing your views

urlpatterns = [
    # Other URLs
    path('add-item/', views.add_item, name='add_item'),

]
