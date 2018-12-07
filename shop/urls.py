from django.urls import path

from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/', views.detail, name='detail'),
]
