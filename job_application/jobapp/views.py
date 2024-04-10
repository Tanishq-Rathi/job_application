from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import JobApplication

def job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            if application.currently_working == 'yes':
                application.eligible = True  # Assuming all 'yes' are eligible
                application.current_ctc = form.cleaned_data['ctc']  # Assuming ctc is a DecimalField in the model
            else:
                application.eligible = False
            application.save()
            return redirect('result', pk=application.pk)
    else:
        form = JobApplicationForm()
    return render(request, 'job.html', {'form': form})

def result(request, pk):
    application = JobApplication.objects.get(pk=pk)
    return render(request, 'result.html', {'application': application})
