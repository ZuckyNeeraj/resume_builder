from django.contrib import admin
from django.urls import path
from resume import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.form, name="index"),
    path('<int:id>/', views.resume, name="resume"),
    path('list/', views.listOfResume, name="list"),
]
