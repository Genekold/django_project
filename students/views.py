from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from students.forms import StudentForms
from students.models import Student, MyModel


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForms
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForms
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:student_list')


class MyModelCreatView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')

    def form_valid(self, form):
        form.instance.created_at = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid()
        response.context_data['error_message'] = 'please correct the errors below'
        return response


class MyModelListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = MyModel
    template_name = 'students/mymodel_list.html'
    context_object_name = 'mymodels'

    def get_queryset(self):
        return MyModel.objects.filter(is_active=True)


class MyModelDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = MyModel
    template_name = 'students/mymodel_detail.html'
    context_object_name = 'mymodel'

    def get_additional_data(self):
        return 'Это дополнительная информация'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = self.get_additional_data()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_active:
            raise Http404("Object not found")
        return obj


class MyModelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'students/mymodel_form.html'
    success_url = reverse_lazy('students:mymodel_list')


class MyModelDeleteView(LoginRequiredMixin, DeleteView):
    model = MyModel
    template_name = 'students/mymodel_confirne_delete.html'
    success_url = reverse_lazy('students:mymodel_list')


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


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/student_list.html', context=context)
