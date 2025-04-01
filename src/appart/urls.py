from rest_framework import routers
from appart.views import AppartViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register('liste', AppartViewSet, basename='liste')

urlpatterns = [
    path('', include(router.urls)),
]