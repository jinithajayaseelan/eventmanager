from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.models import Events
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import NameForm






def get_name(request):

    if request.method == 'POST':
        
        form = NameForm(request.POST)
        if form.is_valid():
           
            return HttpResponseRedirect('/allevents/')

    else:
        form = NameForm()

    return render(request, 'forms.html', {'form': form})



def post_page(request, post_id):
	print(post_id)
	post= Events.objects.get(pk=post_id)
	return render(request,'post.html',{"selected_post":post})

def allevents(request):
	allevents = Events.objects.all()
	return render(request, "allevents.html", {"posts": allevents})


def addevent(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        content = request.POST["content"]


        new_event = Events.objects.create(title=title, content=content)

        return redirect("/allevents/")
    return render(request, "addevent.html")

def form(request, post_id):
    print(post_id)
    event_name=Events.objects.get(pk=post_id)
    if request.method == "POST":
        name=request.POST["name"]
        answer_inst=Events.objects.create(
            answer=answer,
            event_name=event_name,
            author=request.user,
        )

        return redirect("/allevents/")
    return render(request, "forms.html")
    