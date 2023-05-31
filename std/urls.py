from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('home/', home),
    path("add-evt/", evt_add),
    path("delete-evt/<int:name>", delete_evt),
    path("update-evt/<int:name>", update_evt),
    path("do-update-evt/<int:name>", do_update_evt),
    path("evt-detail/<int:name>/", detail),
    path('search/', views.search_events, name='search_events'),
]
