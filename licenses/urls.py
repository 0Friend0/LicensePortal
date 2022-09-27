from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('licenses/', views.licenses, name='licenses'),
    path('licenses/view/<str:pk>/', views.license, name='license'),
    path('licenses/license-add/', views.license_add, name='license-add'),
    path('licenses/license-delete/<str:pk>/', views.license_delete, name='license-delete'),
    path('licenses/license-update/<str:pk>/', views.license_update, name='license-update'),

    path('clients/', views.clients, name='clients'),
    path('clients/view/<str:pk>/', views.client, name='client'),
    path('clients/client-add/', views.client_add, name='client-add'),
    path('clients/client-delete/<str:pk>/', views.client_delete, name='client-delete'),
    path('clients/client-update/<str:pk>/', views.client_update, name='client-update'),

    path('licenses/class-view/', views.LicensesListView.as_view(), name='licenses-view'),
    path('licenses/class-view/<str:pk>/', views.LicenseDetailView.as_view(), name='licenses-view-detail'),
    path('clients/class-view/', views.ClientsListView.as_view(), name='clients-view'),

] 