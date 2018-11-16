from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api, views

app_name = 'dashboard'

router = DefaultRouter()
router.register(r'pages', api.PageViewSet)

apipatterns = router.urls

urlpatterns = [
    path('', views.home, name='home'),
    path('webhook', views.webhook, name='webhook'),
    path('panel/', views.dashboard, name='dashboard'),
    path('api/', include(apipatterns)),

]
