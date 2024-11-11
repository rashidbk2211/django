# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, EducationForm, ExperienceForm, SkillForm, ProjectForm
from .models import Education, Experience, Skill, Project, UserProfile
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Redirect to a success page or another view
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def profile_update(request):
    # Retrieve the latest created UserProfile entry
    latest_profile = UserProfile.objects.latest('id')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES, instance=latest_profile)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Redirect to a success page
    else:
        form = UserRegistrationForm(instance=latest_profile)

    return render(request, 'profile_update.html', {'form': form, 'latest_profile': latest_profile})


def resume(request):
    educations = Education.objects.all()  # Retrieves all education entries

    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Reload the page to display the new entry
    else:
        form = EducationForm()

    return render(request, 'resume.html', {'educations': educations, 'form': form})


def edit_resume(request, id):
    education = get_object_or_404(Education, id=id)  # Retrieve the specific education entry by id

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Redirect back to the resume page after saving
    else:
        form = EducationForm(instance=education)  # Prepopulate form with existing data

    return render(request, 'edit_resume.html', {'form': form, 'education': education})

def experience(request):
    experiences = Experience.objects.all()  # Retrieves all experience entries

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience')  # Reloads the page to display the new entry
    else:
        form = ExperienceForm()

    return render(request, 'experience.html', {'experiences': experiences, 'form': form})


def edit_experience(request, id):
    experience = get_object_or_404(Experience, id=id)  # Retrieve the specific experience entry by id

    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experience')  # Redirect back to the experience page after saving
    else:
        form = ExperienceForm(instance=experience)  # Prepopulate form with existing data

    return render(request, 'edit_experience.html', {'form': form, 'experience': experience})



def skills_view(request):
    skills = Skill.objects.all()  # Retrieve all skill entries from the database

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skills')  # Reloads the page to show the updated skill list
    else:
        form = SkillForm()

    return render(request, 'skills.html', {'skills': skills, 'form': form})


def portfolio(request):
    l_id= UserProfile.objects.all().order_by('-id').first()
    latest_id = l_id.id if l_id else None
    user = UserProfile.objects.get(id=latest_id)
    projects = Project.objects.all()  # Retrieves all projects

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # Include FILES for image uploads
        if form.is_valid():
            form.save()
            return redirect('portfolio')  # Reload the page to display the new entry
    else:
        form = ProjectForm()

    return render(request, 'portfolio.html', {'projects': projects, 'form': form, 'user': user})







# views
def index(request, user_id):
    # Fetch user profile data
    user_profile = get_object_or_404(UserProfile, id=user_id)
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context ={
        'user': user_profile,
        'educations': educations,
        'experiences':experiences,
        'skills': skills,
        'projects': projects,

    }
    return render(request, 'index.html', context)

