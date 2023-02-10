from django.urls import path
from . import views

urlpatterns = [
    path('create_category/', views.CategoryView.as_view()),
    path('create_image/', views.ImageView.as_view()),
    path('create_advertisement/', views.AdvertisementView.as_view())
]