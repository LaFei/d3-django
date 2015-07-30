from django.shortcuts import render

# Create your views here.
from datetime import datetime
from trips.models import Post

def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})

def home(request):
    # get all the posts
    post_list = Post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})