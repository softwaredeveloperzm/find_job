from django.shortcuts import render
from job.models import Job, ApplyJob
from .filter import Jobfilter
from django.http import QueryDict
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    query_params = request.GET.copy()

    for key, value in list(query_params.items()):
        if not value:
            query_params.pop(key)

    available_industries = Job.objects.filter(is_available=True).values_list('industry', flat=True).distinct()
    available_job_types = Job.objects.filter(is_available=True).values_list('job_type', flat=True).distinct()
    available_states = Job.objects.filter(is_available=True).values_list('state', flat=True).distinct()

    class JobFilterClass(Jobfilter):
        class Meta:
            model = Job
            fields = {
                'title': ['icontains'],
                'state': ['exact'],
                'job_type': ['exact'],
                'industry': ['exact'],
            }

    job_filter = JobFilterClass(query_params, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))

    # Paginate your queryset
    paginator = Paginator(job_filter.qs, 4)  # 4 items per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'available_industries': available_industries,
        'available_job_types': available_job_types,
        'available_states': available_states,
        'filter': job_filter,
        'page_obj': page_obj,  # Pass the paginated queryset to the template
    }

    return render(request, 'website/home.html', context)




def job_listing(request):
    filter = Jobfilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))

    #jobs = Job.objects.all()

    context = {'filter': filter}
    return render(request, 'website/job-listing.html', context)


def job_details(request, pk):
    context = {}  # Define context with default values
    
    if request.user.is_authenticated:
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            has_applied = True
        else:
            has_applied = False

        job = Job.objects.get(pk=pk)
        context = {'job': job, 'has_applied': has_applied}
    else:
        messages.info(request, 'Please log in to continue')

    return render(request, 'website/job_details.html', context)
