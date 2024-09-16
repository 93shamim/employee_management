from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages

# Create your views here.


@login_required
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})



@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            # Add success message with username (empID) and password
            messages.success(
                request, 
                f"Employee '{employee.name}' added successfully! His Username: {employee.empID}, and deafult Password: {employee.empID} also created !"
            )
            return redirect('home')
    else:
        form = EmployeeForm()
    
    return render(request, 'employees/add_employee.html', {'form': form})



@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form, 'employee': employee})



@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'employees/delete_employee.html', {'employee': employee})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "employees/login.html", context)



def logout_view(request):
    if request.user.is_authenticated:  
        logout(request) 
    return redirect("login_view")




@login_required
def change_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change

            messages.success(request, "Your password changed successfully!")

            return redirect('home')
    else:
        password_form = PasswordChangeForm(user=request.user)
    
    return render(request, 'employees/change_password.html', {'password_form': password_form})