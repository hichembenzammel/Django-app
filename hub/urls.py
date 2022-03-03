from django.contrib import admin
from django.urls import path
from .views import CreateStudent, coach_list, homePage, student_Details, student_list, StudentListView, \
    StudentDetailView, CreateStudentForm, add_Student, StudentCreateView

urlpatterns = [
    path('home', homePage, name="home"),
    path('index/', student_list, name="studentlist"),
    path('student/', StudentListView.as_view(), name="studentlist1"),
    path('det/', StudentDetailView.as_view(), name="detaillistview"),
    path('coachs/', coach_list, name="coachlist"),
    path('details/<int:id>', student_Details, name="studentdt"),
    path('add/', CreateStudent, name="createStudent"),
    path('addform/', CreateStudentForm, name="createStudentForm"),
    path('adds/', add_Student, name="createStudentFormModel"),
    path('adds1/', StudentCreateView.as_view(), name="createStudentFormModel1"),
]