from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test02/', include('test01_in.urls')),
    path('', RedirectView.as_view(url='/test02/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)