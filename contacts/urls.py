from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contacts import views

urlpatterns = [
    path('contacts/', views.ContactList.as_view()),
    path('contacts/<int:pk>/', views.ContactDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
