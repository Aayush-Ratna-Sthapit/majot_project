from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.projectList, name='index'),  # Handle the empty path with the 'index' view

    path('profile/', views.userProfile, name='user-profile'),

    path('projects', views.projectList, name='projects'),
    path('projects/<int:pk>', views.projectDetail, name='project-detail'), 
    
    path('tasks', views.taskList, name='tasks'),
    path('tasks/<int:pk>', views.taskDetail, name='task-detail'),
    path('create-task', views.taskCreate, name='create-task'),
    path('create-project', views.ProjectCreateView.as_view(), name='create-project'), 

    path('update-task/<int:pk>', views.TaskUpdateView.as_view(), name='update-task'),
    path('update-project/<int:pk>', views.ProjectUpdateView.as_view(), name='update-project'),

    path('delete-task/<int:pk>', views.TaskDeleteView.as_view(), name='delete-task'), 
    path('delete-project/<int:pk>', views.ProjectDeleteView.as_view(), name='delete-project'), 

    path('join-task/<int:pk>', views.joinTask, name='join-task'), 


    path('register', views.registration, name = 'register'),
    path('login', views.UserLoginView.as_view(), name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('update-profile', views.update_profile, name ='update-profile'), 
    path('home/', views.home, name='home'),

    # password reset urls
    path('reset_password', auth_views.PasswordResetView.as_view(template_name = 'users/password-reset.html'), name='password-reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'), name = 'password_reset_done'),
    
    
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-form.html'), name = 'password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html'), name = 'password_reset_complete'),

]
