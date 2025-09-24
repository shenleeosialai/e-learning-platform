# from rest_framework import generics
from courses.api.serializers import SubjectSerializer, CourseSerializer
from courses.models import Subject, Course
from django.db.models import Count
from courses.api.pagination import StandardPagination
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


# class SubjectListView(generics.ListAPIView):
#    queryset = Subject.objects.annotate(
#       total_courses=Count('courses'))
#    serializer_class = SubjectSerializer
#    pagination_class = StandardPagination


# class SubjectDetailView(generics.RetrieveAPIView):
#    queryset = Subject.objects.annotate(
#        total_courses=Count('courses'))
#   serializer_class = SubjectSerializer


class SubjectviewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.annotate(
        total_courses=Count('courses'))
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer
    pagination_class = StandardPagination


class CourseEnrollView(APIView):
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})
