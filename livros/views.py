from django.http import HttpResponse
from .models import livros


def index(request):
    latest_livros_list = livros.objects.order_by('-ano')[:5]
    output = ", ".join([q.titulo for q in latest_livros_list])
    return HttpResponse(output)

def detail(request, livros_id):
    return HttpResponse("You're looking at question %s." % livros_id)


def results(request, livros_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % livros_id)


def vote(request, livros_id):
    return HttpResponse("You're voting on question %s." % livros_id)
