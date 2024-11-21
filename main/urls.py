from django.urls import path
from django.views.generic import TemplateView
from .views import *
from .views import HomeView, RegisterView, ProfileView,CourseListView
CourseDetailView, EnrollView, PaymentListView,UserLoginView
NewsListView, BlogListView, EventListView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView, name='login'),
    path('logout/', logout, name='logoutview'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('event/', EventListView.as_view(), name='event'),
    path('enroll/<int:course_id>/', EnrollView.as_view(), name='enroll'),
    path('payments/', PaymentListView.as_view(), name='payments'),
    path('news/', NewsListView.as_view(), name='news'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('subscribe/', subscribe, name='subscribe'),
    path('search_courses/', search_courses, name='search_courses'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)