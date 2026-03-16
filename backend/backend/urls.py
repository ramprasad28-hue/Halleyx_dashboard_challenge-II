"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from orders import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',views.home),
    path('api/orders/',views.order_list),
    path('api/dashboard/kpi/',views.dashboard_kpi),
    path('api/dashboard/product-revenue/',views.product_revenue),
    path('api/dashboard/order-status/',views.order_status_distribution),
    path('dashboard/',views.dashboard),
    path('api/upload-orders/',views.upload_orders_csv),
    path('orders/',views.orders_page),
    path('api/save-layout/',views.save_layout),
    path('api/load-layout/',views.load_layout),
    path('api/orders/create',views.order_create),
    path('api/orders/<int:pk>/update',views.order_update),
    path('api/orders/<int:pk>/delete',views.order_delete),
    path('configure/',views.configure_page),
]