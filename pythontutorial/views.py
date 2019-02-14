from django.shortcuts import render, HttpResponse
from .models import Post
from django.http import JsonResponse
# Create your views here.


def pythonlang(request):

    data = Post.objects.filter(id=1)

    return render(request, 'python.html', {'data': data})


def python_overview(request, page):

    overview_data = Post.objects.filter(id=page)

    values_list = list(overview_data.values())

    return JsonResponse(values_list, safe=False)
