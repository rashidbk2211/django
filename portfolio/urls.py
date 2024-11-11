# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('resume/', views.resume, name='resume'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills_view, name='skills'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('index/<int:user_id>/', views.index, name='index'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('edit/<int:id>/', views.edit_resume, name='edit_resume'),
    path('edit_experience/<int:id>/', views.edit_experience, name='edit_experience')
]
