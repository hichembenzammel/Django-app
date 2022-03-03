from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from hub.forms import StudentForm, StudentModelForm
from hub.models import Coach, Student


# Create your views here.
def homePage(request):
    return HttpResponse("<h1> Welcome to </h1>")


def student_list(request):
    list = Student.objects.all()
    return render(
        request,
        'hub/index.html',
        {
            'students': list,
        }

    )


class StudentListView(ListView):
    model = Student
    template_name = "hub/index.html"


#  paginate_by = 1

class StudentDetailView(DetailView):
    model: Student
    template_name = "hub/st_details.html"


def coach_list(request):
    list = Coach.objects.all()
    return render(
        request,
        'hub/coach.html',
        {
            'coachs': list,
        }

    )


def student_Details(request, id):
    st = Student.objects.get(id=id)
    return render(
        request,
        'hub/st_details.html',
        {
            'student': st,
        })


# creation du 1er methode de formulaire
def CreateStudent(request):
    print(request)
    if request.method == 'POST':
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        Student.objects.create(
            first_name=firstName,
            last_name=lastName,
            email=email

        )
        return redirect('studentlist1')
    return render(
        request,
        'hub/add_student.html',
    )


def CreateStudentForm(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email')
            )
            # ou bien Student.objects.create(**form.cleaned_data) tektebha wahadha tekhdem les atributs wahadha
            return redirect('studentlist1')
    return render(
        request,
        'hub/add_student.html',
        {
            'form': form,
        }
    )


def add_Student(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('studentlist1')
    return render(
        request,
        'hub/add_student.html',
        {
            'form': form,
        }
    )


# kif el add_student
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'hub/add_student.html'
    """def get_success_url(self):# walla nhotou get_absolute_url(self): return kif kif f class user el model ay update aal user tekhdem
        return redirect('studentlist1')"""
