from django.contrib import admin
from django.urls import path
from houseapp.views import predict_price  # Import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predict_price, name='predict_price'),  # Add the home page route
]
