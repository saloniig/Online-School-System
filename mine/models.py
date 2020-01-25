from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Student(models.Model):

    id = models.AutoField(primary_key=True,blank=True, null=False)
    subject=models.CharField(max_length=100,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    

   
    


class Subject(models.Model):
    id = models.AutoField(primary_key=True,blank=True, null=False)
  #  M1='M1'
   # DE='DE'
    #M2='M2'
    #M3='M3'
   # CN='CN'
    #BEE='BEE'
   # SUBJECT_CHOICES=[
    #    (M1,'M1'),
     #   (DE,'DE'),
      #  (M2,'M2'),
       # (M3,'M3'),
        #(CN,'CN'),
        #(BEE,'BEE'),
    #]

    subject=models.CharField(
        max_length=20,
       # choices=SUBJECT_CHOICES,
        blank=True, null=True


    )
    #ASSIGNMENT='ASSIGNMENT'
   # PAPER='PAPER'
    #STUDYMATERIAL='STUDYMATERIAL'
   # OPTION_CHOICES = [
   # (ASSIGNMENT,'ASSIGNMENT'), 
    #(PAPER, 'PAPER'), 
    #(STUDYMATERIAL,'STUDY MATERIAL'),
   # ] 

   # options = models.CharField( 
    #    max_length = 20, 
     #   choices = OPTION_CHOICES, 
      #  default = '1',blank=True, null=True
      #  )
   # subject_name=models.CharField(max_length=100,blank=True, null=True)
 #   created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
  #  updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
   # deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return self.subject




class Assignment(models.Model):
    id = models.AutoField(primary_key=True,blank=True, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True, null=True)
#   semester = models.ForeignKey(SubjectAndSemester, on_delete=models.CASCADE,blank=True, null=True)
    assignment_no=models.CharField(max_length=100,blank=True, null=True)
    assignment=models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.assignment_no
    


class StudyMaterial(models.Model):
    id = models.AutoField(primary_key=True,blank=True, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True, null=True)
   # semester = models.ForeignKey(SubjectAndSemester, on_delete=models.CASCADE,blank=True, null=True)
    book=models.CharField(max_length=100,blank=True, null=True)
    author=models.CharField(max_length=100,blank=True, null=True)
    details=models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.book



class Paper(models.Model):
    id = models.AutoField(primary_key=True,blank=True, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True, null=True)
    year=models.CharField(max_length=100,blank=True, null=True)
    paper=models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    

    def __str__(self):
        return self.paper


    