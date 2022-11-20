from django.urls import path, include
from rest_framework import routers

from famous_persons import views

router = routers.SimpleRouter()
router.register("person", views.PersonViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("raw-person-list/", views.RawPersonAPIView.as_view(), name="raw-person-list"),
    path(
        "raw-person-list/<int:pk>/",
        views.RawPersonAPIView.as_view(),
        name="raw-person-list-put",
    ),
]
