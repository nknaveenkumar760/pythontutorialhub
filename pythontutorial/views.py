from django.shortcuts import render, HttpResponse
<<<<<<< HEAD
from .models import Post, Video
=======
from .models import Post
>>>>>>> 2182f3a4b8fdddf73aa0b260257e2d329ad6c815
from django.http import JsonResponse
# Create your views here.


def pythonlang(request):

    data = Post.objects.filter(id=1)

    return render(request, 'python.html', {'data': data})


def python_overview(request, page):

    overview_data = Post.objects.filter(id=page)

    values_list = list(overview_data.values())

    return JsonResponse(values_list, safe=False)
<<<<<<< HEAD


def showvideos(request):
    allvideo = Video.objects.all()

    context = {'allvideo': allvideo
               }

    return render(request, 'online_course_video.html', context)
=======
>>>>>>> 2182f3a4b8fdddf73aa0b260257e2d329ad6c815
