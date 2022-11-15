from django.urls import path

from famous_persons import views

urlpatterns = [
    path('personlist/', views.PersonAPIView.as_view(), name='person-list'),
]
