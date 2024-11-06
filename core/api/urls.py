from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from . import views


urlpatterns = [
    #authentication
    path('token/',TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
    path('register/',views.UserRegistrationView.as_view(),name='user_register'),

    #tasks
    path('tasks/',views.TaskListView.as_view(),name = 'task_list'),
    path('tasks/<int:task_id>/',views.TaskDetailView.as_view(),name = 'task_detail'),
]