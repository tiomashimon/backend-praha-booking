
from django.contrib import admin
from django.urls import path, include
from booking.views import BookingViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)