from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('website_api.urls', namespace='website_api')),
    path('', include('website_api.urls', namespace='website_api')),

]
