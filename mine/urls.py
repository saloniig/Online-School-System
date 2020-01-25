from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.Studentform, name='Student'),
    url(r'^search/$', views.Searchform, name='Search'),
    path('sub/', login_required(views.Subjectform), name='Subject'),
    path('ass/', login_required(views.Assignmentform), name='Assignment'),
    path('stu/', login_required(views.StudyMaterialform), name='StudyMaterial'),
    path('pap/', login_required(views.Paperform), name='Paper')



]