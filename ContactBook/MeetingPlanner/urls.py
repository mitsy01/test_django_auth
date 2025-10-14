from django.urls import path

from . import views


urlpatterns = [
    path("", views.get_planners, name="planners"),
    path("get_add_form/", views.get_add_form, name="get_add_form"),
    path("add_planner/", views.add_planner, name="add_planner"),
]