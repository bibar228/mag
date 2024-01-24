"""
URL configuration for mag1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from bizz.views import ProductsViewSet
from trans.views import BillCreateView, TransactionsView
from users.views import base, LoginView, RegistrUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", base),
    path('auth/registr/', RegistrUserView.as_view(), name='registr'),
    path("auth/log/", LoginView.as_view()),
    path("createbill/", BillCreateView.as_view()),
    path("payment/webhook/", TransactionsView.as_view()),
    path("goods/", ProductsViewSet.as_view({'get': 'list'}))
]
