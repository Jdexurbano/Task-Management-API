from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from . import views


urlpatterns = [
    #authentication
    path('token/',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),

    path('',views.get_route,name='sample'),
]