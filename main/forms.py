from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, Subscription

#Create forms for registration and profile updates
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'inn', 'placeholder': 'Email Address',}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'inn', 'placeholder': 'Password',}), required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'inn', 'placeholder': 'Confirm Password',}), required=False)
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class' : 'inn','placeholder' : 'Username',}),
        }
    def save(self, commit=True):
        user = super().save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
       

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['address', 'phone_number', 'course']
        # labels = {
        #     'date_of_birth':'Date Of Birth',
        #     'address':'Address',
        #     'phone_number':'Phone Number',
        #     'course':'Course',
        # }
        widgets = {
            # 'date_of_birth': forms.DateInput(attrs={'class': 'inn', 'placeholder': 'Date Of Birth'}),
            'address': forms.TextInput(attrs={'class': 'inn', 'placeholder': 'Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'inn', 'placeholder': 'Phone Number'}),
            'course': forms.Select(attrs={'class': 'inn', 'placeholder': 'Date Of Birth'}),
        }



class CourseSearchForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'input_field search_form_name',
        'placeholder': 'Course Name'
    }))
    degree = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'input_field search_form_degree',
        'placeholder': 'Degree'
    }))
