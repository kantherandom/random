from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import posts as Posts
import json
from django.contrib import messages

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, "name.html", {"form": form})

def home(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())

def posts(request):
  template = loader.get_template('post.html')
  return HttpResponse(template.render())

def show_form(request):
  context = {}
  context['form'] = PostForm()
  return render(request, "create_post.html", context)

def create_form(request):
  if request.method == "POST":
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.POST['author']
      post.topic = request.POST['topic']
      post.content = request.POST['content']
      post.save()
  return redirect("create_post")

def get_post_by_topic(request, topic):
  posts = Posts.objects.filter(topic=topic)
  return render(request=request, template_name="list_post.html", context={'posts': posts})

# def post_noti(request):
  