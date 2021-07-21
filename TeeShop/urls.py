"""TeeShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static 

from accounts.views import (
    registerPage,
    loginPage,
    logoutPage,
)

from home.views import(
    homePage,
    productDetails
)

from dashboard.views import(
    home_dashboard,
    create_dashboard,
    analysis_dashboard,
    design_view,
    listing_dashboard,
    delete_product
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='home'),
    path('product-details/<int:product_id>', productDetails, name='product_details'),

    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),

    path('dashboard/', home_dashboard, name='homeDashboard'),
    path('dashboard/create/', create_dashboard, name='createDashboard'),
    path('dashboard/create/design', design_view, name='designDashboard'),
    path('dashboard/analysis/', home_dashboard, name='analysisDashboard'),
    path('dashboard/listing/', listing_dashboard, name='listingDashboard'),
    path('dashboard/listing/<int:product_id>', delete_product, name='delete_product'),
         # (?P<product_id>\d+)/$
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
