from django.db import models
from company.models import Company
from users.models import User
from resume.models import Resume



class Job(models.Model):

    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid')
    )

    state_choices = (
        ('Ndola', 'Ndola'),
        ('Lusaka', 'Lusaka'),
        ('Kitwe', 'Kitwe')
    )

    industry_choices = (
        ('IT', 'IT'),
        ('Health', 'Health'),
        ('Finance', 'Finance')
    )


    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)  
    salary = models.PositiveIntegerField(default=3500)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.CharField( max_length=100, choices=state_choices, null=True, blank=True)
    industry = models.CharField( max_length=100, choices=industry_choices, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=job_type_choices, null=True, blank=True)

 

    def __str__(self):
        return self.title
    
class ApplyJob(models.Model):
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title} ({self.status})"

    def save(self, *args, **kwargs):
        # Check if the user has a resume
        if hasattr(self.user, 'resume'):
            # If user has a resume, assign it to the apply job
            self.resume = self.user.resume
            print(f"Resume found for user '{self.user.username}'")
            print(f"Assigned resume: {self.resume}")
        else:
            print(f"No resume found for user '{self.user.username}'")
        super().save(*args, **kwargs)

