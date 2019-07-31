from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from twitterapp import views

urlpatterns = [
    path('users/', views.user_list),
    path('user/<int:pk>/', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)