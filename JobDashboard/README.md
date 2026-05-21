## Pantheon — Job Application Dashboard
A clean, data-driven job application tracking dashboard built with Django. Pantheon helps you manage your job search intelligently — tracking applications, monitoring progress through interview stages, comparing offers, and visualising your success rate in real time.

# Overview
Pantheon gives job seekers a single place to manage their entire application pipeline. From the moment you apply to the moment you receive an offer, every stage is tracked, visualised, and analysed.

# Features

- Application Tracking — Add, update and delete job applications with company, title, salary, location and date applied
  
- Live Stage Updates — Inline dropdown to update application status without leaving the dashboard
  
- Days Since Applied — Each application shows how long ago you applied
  
- Offer Comparison — Side by side salary and location comparison for your top offers
  
- Data Reviewer — Donut chart showing application breakdown by status with live success rate
  
- Welcome Stats — At a glance view of total applications and active interviews
  
- Scrollable Application List — Clean card-based list with custom teal scrollbar
  
- Responsive Design — Adapts cleanly across screen sizes
  
(Tracks interviews as successful due to ROI of use, if rejected after 3rd interview swap to rejected to reformat the true success rate) 


## Installation
# Clone the repository
git clone https://github.com/Bavianx/Django_Projects.git
cd Django_Projects/JobDashboard

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations JobTasks
python manage.py migrate

# Start the server
python manage.py runserver
Then visit http://127.0.0.1:8000/JobTasks/

# V2 Roadmap

- [ ] AI Career Insights — analyse success rate, role types, and salary data to suggest personalised next steps and career path recommendations
- [ ] PostgreSQL — production database replacing SQLite
- [ ] Application Notes — add notes and follow up reminders per application
- [ ] Email Reminders — automated follow up nudges based on days since applied
- [ ] Cover Letter Storage — attach and store tailored cover letters per application
- [ ] Interview Prep — link resources and notes to specific interview stages
- [ ] Export to CSV — download full application history
- [ ] Success Rate Trends — track how your success rate changes over time
- [ ] Company Research Panel — pull company data and news alongside each application
      
## Application Screenshot
<img width="1904" height="908" alt="image" src="https://github.com/user-attachments/assets/d171c1a9-d062-497e-b374-3dbdc69dab9e" />

