from django.urls import path
from .views import *

urlpatterns=[
    path('', EventListView.as_view(), name ="web_home"),

    path('events/<int:pk>/', EventDetailView.as_view(), name ="web_events_detail"),
    path('events/new/', EventCreateView.as_view(), name ="web_events_create"),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name ="web_events_update"),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name ="web_events_delete"),

    path('about/', about, name ="web_about"),
   
]
