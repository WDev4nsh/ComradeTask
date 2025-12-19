from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Main HTML TaskListView
    path('', views.taskList, name = 'tasks'),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name = 'ct_todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),

    # Registration / Create user
    path('register/', views.registerPage, name = 'register'),

    # TaskForm
    path('create-task/', views.createTask, name = 'create-task'),
    path('update-task/<int:pk>/', views.updateTask, name = 'update-task'),
    path('toggle-complete/<int:pk>', views.toggle_complete, name = 'toggle-complete'),

    # TaskDelete (Avadakedavra! HaHaHaHaHa)
    path('delete-task/<int:pk>/', views.deleteTask, name = 'delete-task'),
    path('user/profile/', views.profile_view, name = 'profile-view'),
    path('about-us/', views.about_us, name = 'about-us'),

]
