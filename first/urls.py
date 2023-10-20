from django.urls import path

from .views import CarView, CarDetailView, UserRegistrationView

urlpatterns = [
    path('car/', CarView.as_view(), name='car_brands'),
    path('car/<int:pk>/', CarDetailView.as_view()),
    path('user/registration/', UserRegistrationView.as_view())
]
