from django.urls import include, path
from . import views
from rest_framework import routers

app_name = "courses"
routers = routers.DefaultRouter()
routers.register(r"courses", views.CourseViewSet)
routers.register(r"subjects", views.SubjectviewSet)
urlpatterns = [
    # path("subjects/",
    #     views.SubjectListView.as_view(),
    #     name="subject_list"),
    # path("subjects/<pk>/",
    #    views.SubjectDetailView.as_view(),
    #   name="subject_detail"),
    path("", include(routers.urls)),
    path('courses/<pk>/',
         views.CourseEnrollView.as_view(),
         name='course_enroll'),
]
