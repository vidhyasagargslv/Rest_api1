

from django.urls import path,include
from rest_framework import routers
from app_api.views import StudentViewSet

#?In Django REST Framework, the default router automatically creates the URL conf for your API. 
#?It creates routes for the standard set of list, create, retrieve, update, partial_update, and destroy actions. 
#?It also creates a default API root view for you.


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls))

]