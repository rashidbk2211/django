# forms.py
from django import forms
from .models import UserProfile, Education, Experience, Skill, Project, Testimonial


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'phone', 'birthday', 'location', 'about_me', 'profile_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your location'
            }),
            'about_me': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about yourself'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }



class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['college', 'year', 'description']
        widgets = {
            'college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'College Name'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['worked_field', 'year', 'description']
        widgets = {
            'worked_field': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Worked Field'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
        }




class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'proficiency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skill Name'}),
            'proficiency': forms.NumberInput(attrs={
                'class': 'form-range',
                'type': 'range',
                'min': '0',
                'max': '100',
                'step': '1',
                'value': '50',
            }),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'project_link', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 3}),
            'project_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Project Link'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['photo', 'name', 'description']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your testimonial'
            }),
        }
