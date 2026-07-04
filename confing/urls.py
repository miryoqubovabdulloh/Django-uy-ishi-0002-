from django.contrib import admin
from django.urls import path
from telefon.views import telefon_list, telefon_delete, telefon_edit
from moshina.views import moshina_list, moshina_delete, moshina_edit

urlpatterns = [
    path('tel/', telefon_list, name='telefon_list'),
    path('tel/delete/<int:id>/', telefon_delete, name='telefon_delete'),
    path('tel/edit/<int:id>/', telefon_edit, name='telefon_edit'),
    path('car/', moshina_list, name='moshina_list'),
    path('car/delete/<int:id>/', moshina_delete, name='moshina_delete'),
    path('car/edit/<int:id>/', moshina_edit, name='moshina_edit'),
    path('admin/', admin.site.urls),
]
