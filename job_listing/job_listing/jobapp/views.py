from django.shortcuts import render
from .models import *
from job_listing.settings import BASE_DIR
# Create your views here.

def index(request):
    jobapp = jobapp_info.objects.all()
    return render(request, 'index.html', {'jobapp':jobapp, 'BASE_DIR':BASE_DIR})


def jb(request):
    if request.method == 'POST':
        job = jobapp_info()
        job.job_Post = request.POST.get("job_post", False)
        job.job_Company = request.POST.get("job_company", False)
        job.job_Loc = request.POST.get("job_loc", False)
        job.job_Shift= request.POST.get("job_shift", False)
        job.job_Salary= request.POST.get("job_salary", False)
        job.save()

    
    return render(request, 'upload.html')