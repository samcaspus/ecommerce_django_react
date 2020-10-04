from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns =[
    path('login/', views.signin),
    path('logout/<int:id>',views.signout),
    path('',include(router.urls))
    
]
