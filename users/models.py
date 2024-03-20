from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=True)
    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)

    def __str__(self):
        roles = []
        if self.is_recruiter:
            roles.append('Recruiter')
        if self.is_applicant:
            roles.append('Applicant')
        return f"{self.email} ({', '.join(roles)})"

