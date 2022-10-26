from django.views.generic import ListView
from django.shortcuts import render
from .models import Student


def students_list(request):
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    template = 'school/students_list.html'
    students = Student.objects.all().prefetch_related('teacher')
    result = students.order_by(ordering)
    context = {'object_list': result}
    return render(request, template, context)
