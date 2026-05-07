from django.shortcuts import render, redirect
from .models import Appcontent
from .forms import JobForm
import plotly.express as px

def dashboard(request):
    All_Jobs = Appcontent.objects.all()
    interviews = Appcontent.objects.filter(status__in=['r1', 'r2', 'r3', 'r4', 'final']).count()
    applied_count = Appcontent.objects.filter(status='applied').count()
    rejected_count = Appcontent.objects.filter(status='rejected').count()
    offer_count = Appcontent.objects.filter(status='offer').count()
    interview_count = interviews
    total = Appcontent.objects.count()

    labels = ['Applied', 'Interviewing', 'Offers', 'Rejected']
    values = [applied_count, interview_count, offer_count, rejected_count]

    fig = px.pie(
        names=labels,
        values=values,
        color_discrete_sequence=['#4A9B8E', '#6C8EBF', '#F6AD55', '#FC8181']
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=True,
        height=250
    )

    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

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
        'interviews': interviews,
        'total': total,
        'chart_html': chart_html,
        'applied_count': applied_count,
        'rejected_count': rejected_count,
        'offer_count': offer_count,
        'interview_count': interview_count,
    }
    
    return render(request, 'JobTasks/Dashboardview.html', context)

def update_job(request, pk):
    job = Appcontent.objects.get(id=pk)  #Tags the current request to the ids primary key (single event change rather than all)
    if request.method == 'POST':
        job.status = request.POST['status']  #Changes the field status (new updated event)
        job.save()  
        return redirect('/JobTasks/')


