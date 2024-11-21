from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,  View
from .models import Course, Enrollment, Payment, StudentProfile, News, Blog, Event, Testimonial, Subscription, Course
from .forms import UserRegistrationForm,StudentProfileForm, CourseSearchForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# main views.

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Add your model data to the context
        context['courses'] = Course.objects.all()  # Query the database for all items
        context['testimonials'] = Testimonial.objects.all()  # Query the database for all items
        context['events'] = Event.objects.all()  # Query the database for all items
        return context
    
class EventListView(ListView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'events'


def search_courses(request):
    courses = []

    if request.method=='POST':
        name = request.POST.get('name')
        degree = request.POST.get('degree')

        # Filter courses based on search input
        courses = Course.objects.all()

        if name:
            courses = courses.filter(name__icontains=name)
        if degree:
            courses = courses.filter(degree__icontains=degree)

        print(courses)

    return render(request, 'courses.html', {
        'search_course': courses
    })



class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        studentform = StudentProfileForm()
        return render(request, 'register.html', {'form': form, 'studentform':studentform})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        studentform = StudentProfileForm(request.POST)
        if form.is_valid() and studentform.is_valid():
            user=form.save()
            studentform=studentform.save()
            
            studentform.user=user
            studentform.save()
            
            # messages.success(request, "Your account has been successfully created!")
            return render(request, 'pending_payment.html', {'username': user.username})
        else:
            return render(request, 'register.html', {'form': form, 'studentform':studentform})


def logoutview(request):
    logout(request)
    return redirect('home')


def UserLoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user.studentprofile.made_payment)
            if user.studentprofile.made_payment == False:
                return render(request, 'pending_payment.html', {'username': username})
            else:
                login(request, user)
            
            messages.success(request, f"Welcome, {username}!")
            return redirect('home') # Redirect to the home page or any other page
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home') # Redirect to the home page or any other page

    else:
        return render(request, 'login.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = StudentProfile.objects.get(user=self.request.user)
        return context

class CourseListView(ListView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'courses'
    

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'
    

class EnrollView(LoginRequiredMixin, CreateView):
    model = Enrollment
    fields = []
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.student = StudentProfile.objects.get(user=self.request.user)
        form.instance.course = Course.objects.get(id=self.kwargs['course_id'])
        return super().form_valid(form)

class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'payments.html'
    context_object_name = 'payments'

    def get_queryset(self):
        return Payment.objects.filter(student__user=self.request.user)

class NewsListView(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    paginate_by = 3
    ordering = '-date_posted'

    
class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'testimonial.html'
    context_object_name = Testimonial



def subscribe(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('newsletter_email')
            
            subscribe_ = Subscription.objects.create(email=email)
            subscribe_.save()
            messages.success(request, 'You have subscribed successfully.')
    except:
        messages.error(request, 'The User Email Already Exist.')

    return redirect('home')
