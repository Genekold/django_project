from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from students.models import Student, MyModel


class MyModelCreatView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('mymodel_list')


class MyModelListView(ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object = 'mymodels'


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо {name}! Сообщение получено.")
    return render(request, 'students/contact.html')


def index(request):
    student = Student.objects.get(id=1)
    context = {
        'student_name': f"{student.first_name} {student.last_name}",
        'student_year': student.get_year_display(),
    }
    return render(request, 'students/index.html', context=context)


def student_detail(request):
    student = Student.objects.get(id=1)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)
