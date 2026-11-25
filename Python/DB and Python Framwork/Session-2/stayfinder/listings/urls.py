from django.urls import path
from .views import home, pg_list, pg_detail

urlpatterns = [
    path('', home, name='home'),
    path('pgs/', pg_list, name='pg_list'),
    path('pgs/<int:pg_id>/', pg_detail, name='pg_detail'),
]