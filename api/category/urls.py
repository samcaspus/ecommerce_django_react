from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'', CategoryViewSet)

urlpatterns = [
    path('',include(router.urls))   
]