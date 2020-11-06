from django.conf.urls import url

from .views import (
    MateriListView, 
    MateriDetailView,
    MateriKategoriListView,
    LoginView,
    LogoutView,
    MateriCreate,
    MateriManage,
    MateriDelete,
    MateriEdit,
    search,
)

app_name = 'mysite'
urlpatterns = [
    url('search/', search, name='search'),
    url('logout/',LogoutView, name="logout"),
    url('login/',LoginView, name="login"),
    url('delete/(?P<pk>\d+)', MateriDelete, name="delete"),
    url('edit/(?P<pk>\d+)', MateriEdit, name="edit"),
    url ('manage/', MateriManage, name='manage'),
    url('create/',MateriCreate, name='create'),
    url('kategori/(?P<kategori_input>[^/]+)',MateriKategoriListView.as_view(), name='kategori'),
    url('detail/(?P<pk>\d+)', MateriDetailView.as_view(), name="detail"),
    url('', MateriListView.as_view(), name="list"),  
] 
