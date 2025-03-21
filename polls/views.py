
"""
Vista para resolver peticiones de Polls
"""
from django.db.models import F
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Choice, Question,Answers


class IndexView(generic.ListView):
    """Vista para listar los polls"""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     if request.user.answers_set.filter(question_id=kwargs.get("pk")):
    #         raise Http404
    #     return response

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            "is_anwered": self.request.user.answers_set.filter(
                question=context_data["question"]
            ).exists()
        })
        # print(self.request.user.answers_set.filter(
        #     question=context_data["question"]
        # ).exists())
        print(context_data)
        return context_data
    

    
        


def detail(request, question_id):
    model = Answers
    question = get_object_or_404(Question, pk=question_id)
    
    # Get all answers for the current question
    answers = Answers.objects.filter(question=question).select_related('user')
    
    return render(request, 'polls/detail.html', {'question': question, 'answers': answers})

def cancel_answer(request, answer_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = get_object_or_404(Answers, id=answer_id)
    if request.user == answer.voter:
        answer.delete()
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
   

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
    

class ResultadoView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"





