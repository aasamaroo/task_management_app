from django.urls import path, include

urlpatterns = [
    path('auth/', include('authentication.urls')),  # Routes for user-related endpoints
    path('tasks/', include('tasks.urls')),          # Routes for task-related endpoints
]
