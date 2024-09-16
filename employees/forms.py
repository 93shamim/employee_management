from django import forms
from .models import Employee
from collections import OrderedDict

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'short_description']


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        # Add read-only field if this is an update form
        if self.instance and self.instance.pk:
            self.fields['empID'] = forms.CharField(initial=self.instance.empID, disabled=True, label="Emp.ID")
            self.fields['designation'] = forms.CharField(initial=self.instance.designation, disabled=True, label="Designation")
            self.fields['salary'] = forms.DecimalField(initial=self.instance.salary, disabled=True, label="Salary")

            # Reorder the fields, making empID the first one
            self.fields = OrderedDict(
                [('empID', self.fields['empID'])] + [(key, self.fields[key]) for key in self.fields if key != 'empID']
            )


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone_number