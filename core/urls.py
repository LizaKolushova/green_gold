from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 
from django.contrib import admin
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings


from articles.views import *
from bookings.views import *
from events.views import *
from people.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'fields', FieldViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'events', EventViewSet)
router.register(r'people', PersonViewSet)
router.register(r'people-category', PersonCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("main/", home)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
