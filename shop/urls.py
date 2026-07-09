from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Public website
    path('', views.home, name='home'),
    path('collection/', views.collection, name='collection'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Dashboard (custom admin)
    path('dashboard/login/', views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/sarees/', views.dashboard_saree_list, name='dashboard_saree_list'),
    path('dashboard/sarees/add/', views.dashboard_saree_add, name='dashboard_saree_add'),
    path('dashboard/sarees/<int:pk>/edit/', views.dashboard_saree_edit, name='dashboard_saree_edit'),
    path('dashboard/sarees/<int:pk>/delete/', views.dashboard_saree_delete, name='dashboard_saree_delete'),
    path('dashboard/categories/', views.dashboard_category_list, name='dashboard_category_list'),
    path('dashboard/categories/add/', views.dashboard_category_add, name='dashboard_category_add'),
    path('dashboard/categories/<int:pk>/edit/', views.dashboard_category_edit, name='dashboard_category_edit'),
    path('dashboard/categories/<int:pk>/delete/', views.dashboard_category_delete, name='dashboard_category_delete'),
    path('dashboard/messages/', views.dashboard_messages, name='dashboard_messages'),
]
