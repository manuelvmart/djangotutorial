
from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Choice, Question,Answers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]



class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Get all answers for the current question
    answers = Answers.objects.filter(question=question).select_related('user')
    
    return render(request, 'polls/detail.html', {'question': question, 'answers': answers})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    user = request.user

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        Answers.objects.create(
            question=question,
            choice=selected_choice,
            voter=user
        )
        

        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))