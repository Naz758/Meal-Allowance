from django.urls import path

from . import views

app_name = "meals"

urlpatterns = [
    path("", views.ClaimListView.as_view(), name="claim-list"),
    path("create", views.ClaimCreateView.as_view(), name="claim-create"),
    path("detail/<int:pk>/", views.ClaimDetailView.as_view(), name="claim-detail"),
    path(
        "approve/<int:pk>/",
        views.ClaimApproverCreateView.as_view(),
        name="claim-approve-detail",
    ),
    path("staff/<int:pk>/", views.StaffUpdateView.as_view(), name="staff-update"),
]
