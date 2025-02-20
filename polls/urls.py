from django.urls import include, path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/",include('django.contrib.auth.urls')),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('<int:question_id>/<int:answer_id>/cancel_answer/', views.cancel_answer, name='cancel_answer'),
    path('<int:question_id>/end_answer/', views.end_answer, name='end_answer'),
    path('<int:question_id>/resume_question/', views.resume_question, name='resume_question')
]
