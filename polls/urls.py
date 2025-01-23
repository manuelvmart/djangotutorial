from django.urls import include, path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/",include('django.contrib.auth.urls')),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:pk>/resultado/", views.ResultsView.as_view(), name="resultado"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('<int:question_id>/<int:answer_id>/cancel_answer/', views.cancel_answer, name='cancel_answer'),
        
]
