from api.spectacular.urls import urlpatterns as doc_urls
from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.base')),
]

urlpatterns += doc_urls