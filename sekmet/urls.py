from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import (handler400, handler403, handler404, handler500)

from redir import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.indx_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'redir.views.bad_request'
handler403 = 'redir.views.permission_denied'
handler404 = 'redir.views.page_not_found'
handler500 = 'redir.views.server_error'
