from django.urls import path
from . import views

urlpatterns = [
    # path('app1/', views.index),
    path('', views.login_view, name='login'),
    path('students/', views.view_students, name='view_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:student_id>/update/', views.update_student, name='update_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    path('students/<int:student_id>/teachers/', views.get_teachers, name='get_teachers'),

   path('students/<int:student_id>/assign_teacher/', views.assign_teacher, name='assign_teacher'),
   path('teachers/add/', views.add_teacher, name='add_teacher'),
   path('teachers/', views.view_teachers, name='view_teachers'),
    ]