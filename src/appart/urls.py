from rest_framework import routers
from appart.views import AjouterAppartView, AppartViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register('liste', AppartViewSet, basename='liste')

urlpatterns = [
    path('', include(router.urls)),
    path('ajouter/', AjouterAppartView.as_view(), name='ajouter')
]