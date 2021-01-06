
from django.contrib import admin
from django.urls import path
from formss import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('h1/', views.showformdata),

]
