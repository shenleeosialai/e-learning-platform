from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from courses.models import Course


@login_required
def course_chat_room(request, course_id):
    try:
        course = request.user.courses_joined.get(id=course_id)
    except Course.DoesNotExist:
        return HttpResponseForbidden("Course does not exist.")

    latest_messages = course.chat_messages.select_related(
        "user"
        ).order_by("-sent_on")[
        :50
    ]
    latest_messages = reversed(latest_messages)

    # if request.user not in course.students.all()
    # and request.user != course.instructor:
    # return HttpResponseForbidden("You are not enrolled in this course.")

    return render(
        request,
        "chat/room.html",
        {
            "course": course,
            "latest_messages": latest_messages,
        },
    )
