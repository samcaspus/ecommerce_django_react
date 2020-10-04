from django.urls import include, path
from rest_framework import routers
from .views import OrderViewSet

router = routers.DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    path('add/<str:id>/<str:token>',views.add)
    path('',include(router.urls))   
]