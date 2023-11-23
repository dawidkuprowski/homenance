from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bills/', include('app_bills.urls')),
    path('authentication/', include('authentication.urls'))
]