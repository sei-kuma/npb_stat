from django.contrib import admin
from django.urls import include, path
#from npb_stats.views import IndexTemplateView

urlpatterns = [
#    path('npb_stats/', IndexTemplateView.as_view()),
    path('npb_stats/', include('npb_stats.urls')),
    path('admin/', admin.site.urls),
]
