from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings #画像参照のため追加
from django.contrib.staticfiles.urls import static #画像参照のため追加
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #画像参照のため追加

app_name = 'fashionote'

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'index/', views.Index.as_view(), name='index'),
    path(r'detail/<int:brand_id>', views.detail, name='detail'),
    path(r'create', views.create, name='create'),
    path(r'detail/<int:brand_id>/update',views.update, name="update"),
    path(r'detail/<int:brand_id>/delete',views.delete, name="delete"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

