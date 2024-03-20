from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .form import CreateJobForm, UpdateJobForm
from company.models import Company
from .models import Job, ApplyJob
from resume.models import Resume
from django.shortcuts import render, redirect, get_object_or_404



def create_job(request):
    if request.user.is_authenticated:
        if request.user.is_recruiter and request.user.has_company:
            if request.method == 'POST':
                form = CreateJobForm(request.POST)
                if form.is_valid():
                    job = form.save(commit=False)
                    job.user = request.user
                    try:
                        user_company = Company.objects.get(user=request.user)
                        job.company = user_company
                        job.save()
                        messages.success(request, 'New Job Has Been Created.')
                        return redirect('dashboard')
                    except Company.DoesNotExist:
                        messages.warning(request, 'User does not have a company.')
                else:
                    messages.warning(request, 'Form is not valid. Something went wrong.')
            else:
                form = CreateJobForm()
            context = {'form': form}
            return render(request, 'job/create-job.html', context)
        else:
            messages.warning(request, 'Permission Denied')
            return redirect('dashboard')
    else:
        return redirect('login')



    
#update a job
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your Job Has Been Updated..')

        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
        return render(request, 'job/update-job.html', context)
    

def manage_job(request):
    total_applicant = ApplyJob.objects.count()
    print(total_applicant)

    # Get all jobs associated with the current user
    jobs = Job.objects.filter(user=request.user)

    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        job = Job.objects.get(id=job_id)
        job.is_available = not job.is_available
        job.save()
        return redirect('manage_job')  # Redirect back to the manage_job view after updating job availability

    # Iterate through each job to retrieve the first name of each applicant
    for job in jobs:
        # Retrieve all ApplyJob instances related to the current job
        apply_jobs = ApplyJob.objects.filter(job=job)

        # Iterate through each ApplyJob instance
        for apply_job in apply_jobs:
            # Retrieve the user associated with the apply_job
            user = apply_job.user
            
            # Check if the user has a resume and retrieve the first_name if available
            if hasattr(user, 'resume'):
                first_name = user.resume.first_name
                # Print the first name to the console
                print(f"First name of the applicant for job '{job.title}': {first_name}")

    context = {'jobs': jobs, 'total_applicant': total_applicant}
    return render(request, 'job/manage-jobs.html', context)





def apply_to_job(request, pk):
    if request.user.is_authenticated:
        job = Job.objects.get(pk=pk)
        ApplyJob.objects.create(
            job=job,
            user=request.user,
            status='Pending'
        )

        messages.info(request, 'You have successfully applied! Please see dashboard')
        # Redirect to the job details page for the applied job
        return redirect(reverse('job_details', kwargs={'pk': pk}))
    
    else:
        messages.info(request, 'Please log in to continue')
        # Redirect back to the job details page without applying
        return redirect(reverse('job_details', kwargs={'pk': pk}))
    

def all_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk)
    applicants = job.applications.all()
    applicant_info = []

    for applicant in applicants:
        user = applicant.user
        try:
            resume = Resume.objects.get(user=user)
            applicant_info.append({
                'first_name': resume.first_name,
                'surname': resume.surname,
                'resume_url': resume.upload_resume.url if resume.upload_resume else None,
            })
        except Resume.DoesNotExist:
            applicant_info.append({
                'first_name': "No resume found",
                'surname': "No resume found",
                'resume_url': None,
            })

    # Zip applicants and applicant_info together
    applicant_data = zip(applicants, applicant_info)
    
    context = {'job': job, 'applicant_data': applicant_data}
    return render(request, 'website/all_applicants.html', context)

def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs': jobs}
    return render(request, 'job/applied_job.html', context)



