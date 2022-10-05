from gettext import install
from django.shortcuts import redirect, render
from students.forms import StudentForm

from students.models import Student

# Create your views here.


def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})


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
