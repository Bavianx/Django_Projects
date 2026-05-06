from django.shortcuts import render, redirect
from .models import Appcontent
from .forms import JobForm

def dashboard(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
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





