"""
URL configuration for E_learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from E_learning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('courses/',views.courses,name='courses'),
    path('instructor/',views.instructor,name='instructor'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('single/',views.single,name='single'),
    path('single2/',views.single2,name='single2'),
    path('single3/',views.single3,name='single3'),
    path('single4/',views.single4,name='single4'),
    path('single5/',views.single5,name='single5'),
    path('single6/',views.single6,name='single6'),
    path('single7/',views.single7,name='single7'),
    path('single8/',views.single8,name='single8'),
    path('single9/',views.single9,name='single9'),
    path('single10/',views.single10,name='single10'),
    path('single11/',views.single11,name='single11'),
    path('single12/',views.single12,name='single12'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('logout/', views.logout, name='logout'),
]
