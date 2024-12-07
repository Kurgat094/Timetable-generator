from django.shortcuts import render, redirect
from .models import Teacher,Unit
from .forms import TeacherForm,UnitForm

def admins(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admins")
    else:
        form = TeacherForm()
    teachers = Teacher.objects.all()
    return render(request, "admin.html", {"form": form, "teachers": teachers})

def register_unit(request):
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_unit")
    else:
        form = UnitForm()
    units = Unit.objects.all()
    return render(request, "register_unit.html", {"form": form, "units": units})