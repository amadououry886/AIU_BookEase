from django.urls import path
from facilities.views import FacilityListView, FacilityDetailView

urlpatterns = [
    path('', FacilityListView.as_view(), name='facility-list'),
    path('<int:id>/', FacilityDetailView.as_view(), name='facility-detail'),
]
