from .models import Project

from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from .forms import UploadForm


def get_project(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/')
    else:
        form = UploadForm()

    return render(request, 'projects/upload_project.html', {'form': form})


class ProjectListView(ListView):
    model = Project
