from django.urls import path

from famous_persons import views

urlpatterns = [
    path("person-list/", views.PersonListAPIView.as_view(), name="person-list"),
    path(
        "person-retrieve-update-destroy/<int:pk>/",
        views.PersonCRUDAPIView.as_view(),
        name="person-crud",
    ),
    path(
        "person-list-create/",
        views.PersonListCreateAPIView.as_view(),
        name="person-list-create",
    ),
    path("raw-person-list/", views.RawPersonAPIView.as_view(), name="raw-person-list"),
    path(
        "raw-person-list/<int:pk>/",
        views.RawPersonAPIView.as_view(),
        name="raw-person-list-put",
    ),
]
