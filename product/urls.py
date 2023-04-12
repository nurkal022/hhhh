from django.urls import path
from rest_framework import routers

from . import views
from .api import *

router=routers.DefaultRouter()
router.register('api/product',ProductViewSet,"product")

urlpatterns=router.urls
urlpatterns=list(urlpatterns)


