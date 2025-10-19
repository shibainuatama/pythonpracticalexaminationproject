from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-secret-internal-panel-for-shibainuatama/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
]
