from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from rest_framework_test import routers
# from quickstart import views
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),

    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework_test.urls', namespace='rest_framework_test'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# this we able login, logout authintcions
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
