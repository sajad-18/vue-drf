from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/items/', views.QuestionListView.as_view(), name='questions_list'),
    path('question/create/', views.QuestionCreateView.as_view(), name='create_question'),
    path('question/update/<int:pk>/', views.QuestionUpdateView.as_view(), name='update_question'),
    path('question/del/<int:pk>/', views.QuestionDeleteView.as_view(), name='delete_question'),
]
