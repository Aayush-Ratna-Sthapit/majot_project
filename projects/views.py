from django.shortcuts import render,redirect
from .models import *
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Count

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView
# Create your views here.

#-------------------------------------User Profile-----------------------------------------------------------

@login_required
def userProfile(request):
    curr_user = request.user
    profile = Profile.objects.get(user=curr_user)
    context = {
        'profile': profile,
    }
    return render(request, 'projects/userProfile.html', context)

#-----------------------------------Display Lists--------------------------------------------------------------

@login_required
def projectList(request):
   projects = Project.objects.all()
  
   context = {'projects':projects}
   return render(request, 'projects/projects.html',context)


@login_required
def projectDetail(request,pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {'project':project,'project_tasks':project_tasks}
   return render(request, 'projects/project-detail.html',context)


@login_required
def taskList(request):
    tasks = Task.objects.all()
    assignees = Profile.objects.filter(task__isnull=False).distinct()

    context = {'tasks': tasks, 'assignees': assignees}
    return render(request, 'projects/tasks.html', context)


@login_required
def taskDetail(request,pk):
  task = Task.objects.get(id=pk)
  context = {'task':task}
  return render(request, 'projects/task-detail.html',context)

def userList(request):
    users = Profile.objects.all()
    context = {'users': users}
    return render(request, 'projects/users.html', context)

#-----------------------------------------CUD views----------------------------------------------------

@login_required
def taskCreate(request):
   form = TaskForm
   if request.method == "POST":
       form =TaskForm(request.POST)
       if form.is_valid():
           form.save()   
           return redirect('tasks')

   context = {'form':form}
   return render(request, 'projects/task-create.html',context)


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = ["name","description"]
    template_name = 'projects/project_create_form.html'
    success_url = reverse_lazy('projects')
   

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'projects/project_update_form.html'
    fields = ["name","description"]
    success_url = reverse_lazy('projects')


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'projects/task_update_form.html'
    fields = ["title","description","project","assignee","due_date","status"]
    success_url = reverse_lazy('tasks')



class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('projects')


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'projects/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')


@login_required
def joinTask(request,pk):
   task =Task.objects.get(id=pk)
   task.assignee=request.user
   task.save()
   return redirect('tasks')
    



# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html',context)

def registration(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('home')

    form = UserCreationForm
    context = {'form':form}
    return render(request, 'users/registration.html', context)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form = AuthenticationForm

def logout_user(request):
    logout(request)
    return redirect("login")

# users/views.py
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def update_profile(request):
   if request.method == 'POST':
       form = ProfileForm(request.POST, instance=request.user.profile)
       if form.is_valid():
           form.save()
           return redirect('tasks')
   else:
       form = ProfileForm(instance=request.user.profile)
  
   context = {'form': form}
   return render(request, 'users/profile-update-form.html', context)


from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'base.html')
 
def projects(request):
  return render(request, 'projects/projects.html')


from .forms import ProfileForm, UserForm
from django.contrib.auth.models import User

def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        user_form = UserForm(request.POST)

        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('user-list')

    else:
        profile_form = ProfileForm()
        user_form = UserForm()

    context = {
        'profile_form': profile_form,
        'user_form': user_form,
    }

    return render(request, 'users/create-profile.html', context)