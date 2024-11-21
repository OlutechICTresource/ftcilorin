from django.db import models
from django.contrib.auth.models import User

# main models.

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING, null=True, blank=True)
    made_payment = models.BooleanField(default=False)


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=50)
    course_unit = models.IntegerField(default=1)  # Set default units if applicable
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True, blank=True)
    author_image = models.ImageField(upload_to='authors/', null=True, blank=True)
    course_image = models.ImageField(upload_to='courses/')
    degree = models.CharField(max_length=255, null=True, blank=True)
 
    def __str__(self):
        return self.title

    
class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/')  # Adjust path as necessary

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

class Payment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='News/', null=True, blank=True)

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


class Subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
