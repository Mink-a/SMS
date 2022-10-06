from django.http import HttpResponse
from django.shortcuts import redirect, render
from students.forms import StudentForm

from students.models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from students.resources import StudentResource
from students.filters import StudentFilter

from tablib import Dataset

# Create your views here.


def index(request):
    f = StudentFilter(request.GET, queryset=Student.objects.all())
    return render(request, 'students/index.html', {'students': f})


def view_student(request, id):
    student = Student.objects.get(id=id)
    return redirect('home', {'student': student})


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_student_first_name = form.cleaned_data['first_name']
            new_student_last_name = form.cleaned_data['last_name']
            new_student_email = form.cleaned_data['email']
            new_student_field_of_study = form.cleaned_data['field_of_study']
            new_student_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number=new_student_number,
                first_name=new_student_first_name,
                last_name=new_student_last_name,
                email=new_student_email,
                field_of_study=new_student_field_of_study,
                gpa=new_student_gpa
            )

            new_student.save()
            return render(request, 'students/addForm.html', {'form': form, 'success': True})
    else:
        form = StudentForm()
        return render(request, 'students/addForm.html', {'form': form})


def update(request, id):
    if request.method == 'POST':
        student = Student.objects.get(id=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/addForm.html', {'form': form, 'success': True})
    else:
        student = Student.objects.get(id=id)
        form = StudentForm(instance=student)
        return render(request, 'students/updateForm.html', {'form': form})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')

def export(request):
    student_resource = StudentResource()
    f = StudentFilter(request.GET, queryset=Student.objects.all())
    dataset = student_resource.export(f.qs)
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Students.xls"'
    return response

def upload(request):
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = student_resource.import_data(
            dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            student_resource.import_data(
                dataset, dry_run=False)  # Actually import now

    return redirect('home')
