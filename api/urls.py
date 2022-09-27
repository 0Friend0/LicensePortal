from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiHome.as_view()),
    path('clients/', views.clients.as_view()),
    path('clients/<str:pk>', views.clientDetails.as_view()),
    path('licenses/', views.licenses.as_view()),
    path('licenses/<str:pk>', views.licenseDetails.as_view()),


]
