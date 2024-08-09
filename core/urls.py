"""
Default Urls
"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # Apps
    path('', include('main.urls')),
    path('auth/', include('users.urls', namespace='auth')),
    path('bursary/', include('bus.urls', namespace='bus')),
    path('student/', include('std.urls', namespace='std')),


    # Package
    path("__reload__/", include("django_browser_reload.urls")),
]
