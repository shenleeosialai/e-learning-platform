from django.db.models import Count
from rest_framework import serializers
from courses.models import Subject, Course, Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["id", "title", "description"]


class SubjectSerializer(serializers.ModelSerializer):
    total_courses = serializers.IntegerField(read_only=True)
    popular_courses = serializers.SerializerMethodField()

    def get_popular_courses(self, obj):
        courses = (
            obj.courses.annotate(total_students=Count("students"))
            .order_by("-total_students")[:3]
        )
        return [f"{c.title} ({c.total_students})" for c in courses]

    class Meta:
        model = Subject
        fields = [
            "id",
            "title",
            "slug",
            "total_courses",
            "popular_courses",
        ]


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "slug", "overview",
                  "subject", "created", "owner", "modules"]
