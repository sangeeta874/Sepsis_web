from django import forms
from .models import TestReport
class TestReportForms(forms.ModelForm):
    class Meta:
        model=TestReport
        fields=['Age','HR','O2Sat','Temp','SBP','DBP','Resp']
