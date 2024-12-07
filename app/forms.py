from django import forms
from .models import Teacher,Unit

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "email", "subject"]


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ["name", "code", "description", "teacher"]