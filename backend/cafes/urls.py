from django.urls import path

from cafes import views

urlpatterns = [path("reviews/", views.CafeReview, name="cafe-review")]
