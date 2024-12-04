from django.shortcuts import render, get_object_or_404,redirect
from .models import Student,Log,Teacher
from django.utils import timezone
from django.contrib import messages

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        student = Student.objects.create(name=name, age=age)
        return redirect('view_students')
    return render(request, 'add_student.html')

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.save()
        return redirect('view_students')
    return render(request, 'update_student.html', {'student': student})
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('view_students')

def get_teachers(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    teachers = student.teachers.all()
    return render(request, 'view_teachers.html', {'teachers': teachers})

def login_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        log_sign_in(name,password)  # Calling function to log sign-in event
        return redirect('view_students')  # Redirect to students list or a dashboard
    return render(request, 'login.html')

def log_sign_in(name,password):
    log_entry = Log(name=name, signed_in_at=timezone.now(),password=password)
    log_entry.save()


def assign_teacher(request, student_id):
    student = get_object_or_404(Student, id=student_id)  # Get the student by ID
    teachers = Teacher.objects.all()  # Get all teachers to display as options

    if request.method == 'POST':
        teacher_ids = request.POST.getlist('teachers')  # Get list of selected teacher IDs
        selected_teachers = Teacher.objects.filter(id__in=teacher_ids)  # Get teachers by IDs
        student.teachers.set(selected_teachers)  # Assign selected teachers to the student
        student.save()  # Save the student object with the updated teachers
        return redirect('view_students')  # Redirect to the students list

    return render(request, 'assign_teacher.html', {'student': student, 'teachers': teachers})


def add_teacher(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']

        # Create a new teacher
        teacher = Teacher(name=name, subject=subject)
        teacher.save()

        # Add a success message and redirect
        messages.success(request, f'Teacher {name} added successfully!')
        return redirect('view_teachers')  # Redirect to the teacher list or another page

    return render(request, 'add_teacher.html')  # Render the teacher addition form
def view_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'view_teachers.html', {'teachers': teachers})