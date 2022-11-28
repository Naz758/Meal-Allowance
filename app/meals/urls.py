from django.urls import path

from . import views

app_name = "meals"

urlpatterns = [
    path("", views.ClaimListView.as_view(), name="claim-list"),
    path("create", views.ClaimCreateView.as_view(), name="claim-create"),
    path("detail/<int:pk>/", views.ClaimDetailView.as_view(), name="claim-detail"),
    path("update/<int:pk>/", views.ClaimUpdateView.as_view(), name="claim-update"),
    path('pdf/<int:pk>/', views.render_pdf_view, name='pdf')
]
