
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .models import Subject, Paper
from django.core.serializers import serialize
   


def Searchform(request):
    if request.method=='GET':
        subject_id=request.GET['subject']
        model = request.GET["option"]
        model =globals()[model]
        searchpost=model.objects.filter(subject_id=subject_id)
        #pdb.set_trace()
        searchpost=serialize('json', searchpost)
        #response_dict = {
         #       "searchpost":searchpost
          #      }
#        m=Student(mine=searchpost)
        return HttpResponse(searchpost)
    else:
        return HttpResponse("not success")




    
def Studentform(request):
   # if request.method == 'POST':
    #        subject_id= request.GET['subject_id']
     #       likedpost = Subject.obejcts.get(pk=subject_id) #getting the liked posts
      #      m = Student(mine=likedpost) # Creating Like Object
               #m.save()  # saving it to store in database
       #     return HttpResponse("Success!") # Sending an success response
# else:
   #         return HttpResponse("Request method is not a GET")
    subject_objects = Subject.objects.all()
    return render(request, "mine/Student.html",{"subject_objects":subject_objects})    

    #return render(request, 'mine/Subject.html')

def Subjectform(request):
    if request.method== "POST":             
        form= SubjectForm(request.POST)     
        temp = request.POST['subject']
        if form.is_valid():
            subject_objects = Subject.objects.all()


            field = request.POST.get('options')
            if field == "PAPER":

                return render(request, "mine/Paper.html",{"temp":temp, "subject_objects":subject_objects})
            elif field == "ASSIGNMENT":
                return render(request, "mine/Assignment.html",{"temp":temp, "subject_objects":subject_objects})
            else:
                return render(request, "mine/StudyMaterial.html",{"temp":temp, "subject_objects":subject_objects})
        return render(request, "mine/Subject.html",{"temp":temp})
  #  subject_object = Subject.objects.all()
    subject_objects = Subject.objects.all()
    
    return render(request, 'mine/Subject.html',{"subject_objects":subject_objects})

def Assignmentform(request):
    if request.method== "POST":             
        form= AssignmentForm(request.POST)     
        form.save()
    
        return HttpResponse('Thanks!!')


    return render(request, 'mine/Assignment.html')
    
def StudyMaterialform(request):
    if request.method== "POST":             
        form= StudyMaterialForm(request.POST)     
        form.save()

        return HttpResponse('Thanks!!')

    return render(request, 'mine/StudyMaterial.html',{"temp":temp})
def Paperform(request):
    if request.method== "POST":             
        form= PaperForm(request.POST)     
        form.save()
        return HttpResponse('Thanks!!')

    return render(request, 'mine/Paper.html',{"temp":temp})
    
