from django.contrib import admin
from django.urls import path
from products_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/',ProductListView.as_view(), name='get'),
    path('post/',PostDetail.as_view(), name='post'),
    path('put/',PutViewSet.as_view(), name='put'),
]
