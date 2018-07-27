from django.urls import path
from .function_based_views import start_job, jobs


urlpatterns = [
    path('startjob/', start_job),
    path('jobs/<id>', jobs),
]