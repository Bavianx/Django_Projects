from django.shortcuts import render, redirect
from .models import Appcontent
from .forms import JobForm

def dashboard(request):
    if request.method == 'POST':
        form = JobForm(request.POST) #Form collects all data
        print(form.errors)
        if form.is_valid():     
            form.save()
            return redirect('/JobTasks/')  

    All_Jobs = Appcontent.objects.all()
    form = JobForm()

    context = {
        'gatherjobs': All_Jobs,
        'forms': form, 
    }
    
    return render(request, 'JobTasks/Dashboardview.html', context)

def update_job(request, pk):
    job = Appcontent.objects.get(id=pk)  #Tags the current request to the ids primary key (single event change rather than all)
    if request.method == 'POST':
        job.status = request.POST['status']  #Changes the field status (new updated event)
        job.save()  
        return redirect('/JobTasks/')



