from rest_framework import routers
from appart.views import AppartementViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register('liste', AppartementViewSet, basename='liste')

urlpatterns = [
    path('', include(router.urls))
]