
from django.urls import path
from .views import *

urlpatterns = [
    path('stringinfo/', AddAndGetStringData.as_view(), name="get_users"),
    path('stringoperation/', StringOperations.as_view(), name="get_users"),
    path('getactivitylog/', Activitylog.as_view(), name="get_users"),
    
   
   
]
