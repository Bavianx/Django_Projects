from django.shortcuts import render, redirect
from .models import Appcontent
from .forms import JobForm
import plotly.express as px
from django.utils import timezone
from datetime import date

def dashboard(request):
    All_Jobs = Appcontent.objects.all()
    interviews = Appcontent.objects.filter(status__in=['r1', 'r2', 'r3', 'r4', 'final']).count()
    applied_count = Appcontent.objects.filter(status='applied').count()
    rejected_count = Appcontent.objects.filter(status='rejected').count()
    offer_count = Appcontent.objects.filter(status='offer').count()
    interview_count = interviews
    total = Appcontent.objects.count()

    labels = ['Applied', 'Interviewing', 'Offers', 'Rejected'] #Key map for colours
    values = [applied_count, interview_count, offer_count, rejected_count] #key map integer counter
    
    success_rate = round(((interview_count + offer_count) / total * 100), 1) if total > 0 else 0 #Success rate = getting an interview or offer 
    offers = Appcontent.objects.filter(status ='offer')
    
    fig = px.pie(
        names=labels,   #Ties colour to the labels
        values=values,  #Ties values to the count
        hole=0.5
    )

    fig.update_traces(
        marker=dict(colors=['#4A9B8E', '#6C8EBF', '#F6AD55', '#FC8181']), #Bypassed the plotly colour charting logic as it was missmatch prior
        textinfo='none',
        hovertemplate='%{label}: %{value}<extra></extra>'
    )

    fig.add_annotation(
        text=f"{success_rate}%<br><span style='font-size:10px'>SUCCESS</span>",
        x=0.5, y=0.5,
        font_size=16,
        showarrow=False
    )
    fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0),
    coloraxis_showscale=False,
    height=150,
    showlegend=False
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

    jobs_with_days = []
    for job in All_Jobs:
        if job.date:
            days_ago = (date.today() - job.date).days
            if days_ago == 0:
                time_label = "Today"
            elif days_ago == 1:
                time_label = "1 day ago"
            else:
                time_label = f"{days_ago} days ago"
        else:
            time_label = "Date Unknown"
        jobs_with_days.append({
            'job': job,
            'time_label': time_label
        })

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
        'success_rate': success_rate,
        'offers': offers,
        'jobs_with_days': jobs_with_days,
    }
    
    return render(request, 'JobTasks/Dashboardview.html', context)

def update_job(request, pk):
    job = Appcontent.objects.get(id=pk)  #Tags the current request to the ids primary key (single event change rather than all)
    if request.method == 'POST':
        job.status = request.POST['status']  #Changes the field status (new updated event)
        job.save()  
        return redirect('/JobTasks/')
    
def delete_job(request, pk):
    job = Appcontent.objects.get(id=pk)  #Tags the current request to the ids primary key (single event change rather than all)
    if request.method == 'POST':
        job.delete()  
        return redirect('/JobTasks/')


