from django.urls import path
from .views import (
    AirportRouteCreateView,
    LastReachableNodeView,
    DurationResultView,
    HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AirportRouteCreateView.as_view(), name='add-route'),
    path('search/', LastReachableNodeView.as_view(), name='search-route'),
    path('results/', DurationResultView.as_view(), name='results'),
]
