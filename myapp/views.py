from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Feed, Like, Unlike
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "base.html")
    # return HttpResponse("Hello")

def signup(request):
    if request.method == "POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        email = request.POST['email']
        pswd = request.POST['pswd']

        myuser = User.objects.create_user(uname, fname, pswd)
        myuser.first_name = fname
        myuser.save()

        return redirect("home")

    else:
        return HttpResponse("404 - Not Found")

def Login(request):
    if request.method=="POST":
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(username=uname, password=pswd)

        if user is not None:
            login(request, user)
            return redirect("feed")
        else:
            return HttpResponse("Invalid Credentials")
    
    return HttpResponse("404 - Not Found")

def Logout(request):
    logout(request)
    return redirect('home')

@login_required()
def feed(request):
    feeds = Feed.objects.all()
    user = request.user
    return render(request, "feed.html",{'feeds':feeds, 'user':user})

@login_required
def liked_post(request):
    user = request.user
    if request.method == "POST":
        feed_id = request.POST['feed_id']
        feed_obj = Feed.objects.get(id=feed_id)

        if user in feed_obj.unliked.all():
            feed_obj.unliked.remove(user)
            
        if user in feed_obj.liked.all():
            feed_obj.liked.remove(user)
        else:
            feed_obj.liked.add(user)
        
        like, create = Like.objects.get_or_create(user=user, feed_id=feed_id)

        if not create:
            if like.value == 'like':
                like.value = 'unlike'
            else:
                like.value = 'like'

        like.save()
        return redirect('feed')

@login_required
def unliked_post(request):
    user = request.user
    if request.method == "POST":
        feed_id = request.POST['feed_id']
        feed_obj = Feed.objects.get(id=feed_id)

        if user in feed_obj.liked.all():
            feed_obj.liked.remove(user)

        if user in feed_obj.unliked.all():
            feed_obj.unliked.remove(user)
        else:
            feed_obj.unliked.add(user)
        
        unlike, create = Unlike.objects.get_or_create(user=user, feed_id=feed_id)

        if not create:
            if unlike.value == 'unlike':
                unlike.value = 'like'
            else:
                unlike.value = 'unlike'

        unlike.save()
        return redirect('feed')