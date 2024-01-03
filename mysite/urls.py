from django.contrib import admin
from django.urls import path
from myapp.views import DemonstrateList,DemonstrateDetail

urlpatterns = [
    path('api/Demonstrate',DemonstrateList.as_view()),
    path('api/Demonstrate/<int:pk>',DemonstrateDetail.as_view()),
    path('admin/', admin.site.urls),
]
