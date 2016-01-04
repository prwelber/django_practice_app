from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Question
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """ return the last five published questions (not including
        those set to be published in the future) """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        # .filter(pub_date)__lte=timezone.now() returns Questions whose pub_date are less than or equal to (lte) timezone.now()


# THIS IS THE OLD INDEX VIEW
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))
#     # or a shortcut is to use the render() function, which takes three arguments
#     # this means you don't have to load the template
#     # return render(request, 'polls/index.html', context)


# THIS IS THE OLD DETAIL VIEW
# def detail(request, question_id):
#     try:
#       question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#       raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#     # or a shortcut is to use the get_object_or_404() function, which takes first argument a Django Model (in this case Question) and an abritrary number of keyword args after that, which are passed to the get() function in the model manager..here is the example:
#     # question = get_object_or_404(Question, pk=question_id)
#     # which replaces the try accept and raise lines
#     # this essentially says get model object according to primary key, and if it doesn't exist, raise a 404 error

# THIS IS THE OLD RESULTS VIEW
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# NEW GENERIC DETAIL AND RESULTS VIEW

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(self, request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question
                                            .id,)))
