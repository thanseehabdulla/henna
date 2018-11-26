# from django.conf.urls import include, url  # < Django-2.0
from django.contrib import admin
from django.urls import include, path  # > Django-2.0
from oscar.app import application
from onlineshop.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    # url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),  # > Django-2.0

    # url(r'', application.urls),
    path('', application.urls),  # > Django-2.0
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

# if settings.DEBUG:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Serve static and media files from development server
urlpatterns += staticfiles_urlpatterns()

