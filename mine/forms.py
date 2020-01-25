from django import forms
#from mine.models import Subject
#from mine.models import SubjectAndSemester

from mine.models import *

class SubjectForm(forms.ModelForm):

    class Meta:
        model=Subject
        fields = ['subject']


class AssignmentForm(forms.ModelForm):

    class Meta:
        model=Assignment
        fields = ["subject",'assignment_no', 'assignment']

class StudyMaterialForm(forms.ModelForm):

    class Meta:
        model=StudyMaterial
        fields = ["subject",'book', 'author','details']
class PaperForm(forms.ModelForm):

    class Meta:
        model=Paper
        fields = ["subject",'year', 'paper']
class StudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields = ['subject']
   # def __init__(self, *args, **kwargs):
    #    super(SubjectForm, self).__init__(self, *args, **kwargs)
        #self.helper=FormHelper()
        #self.helper.form_method="POST"