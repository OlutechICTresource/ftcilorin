from django.contrib import admin
from .models import StudentProfile, Course, Enrollment, Payment, News, Blog, Testimonial, Event

# Register main models.

admin.site.register(StudentProfile)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Payment)
admin.site.register(News)
admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Event)