from django.urls import path

from famous_persons import views

urlpatterns = [
    path("person-list/", views.PersonAPIView.as_view(), name="person-list"),
    path("raw-person-list/", views.RawPersonAPIView.as_view(), name="raw-person-list"),
    path("raw-person-list/<int:pk>/", views.RawPersonAPIView.as_view(),
         name="raw-person-list-put"),
]
