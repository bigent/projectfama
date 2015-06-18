# -*- coding: utf-8 -*-
import json, sys
import time
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.uploadhandler import FileUploadHandler
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from django.template.context import RequestContext
from website.models import Fama, Reporter
import foursquare
from django.contrib.auth.views import login
from website.forms import FamaForm, UserForm, ReporterForm, ChangeEmailForm, MyPasswordChangeForm, TicketForm, ChangeProfilePictureForm

#---begin--- foursquare client id and client secret
client_id = "A3VXW30IK3MVYL3AYPA0GFXDK4VTPTSAT5SWANKDOJQVN0CY"
client_secret = "FTVVMZNWM4RRO2HI4RKEB3EH11AFPFAZTFKIKK5YCXGTLQ2A"
#---stop---


#foursquare config
client = foursquare.Foursquare(client_id=client_id, client_secret=client_secret, version=time.strftime("%Y%m%d"))


#---begin--- this function can request data from foursquare in secret
def search_places(request):
    try:
        if request.method == "GET" and 'query' in request.GET:
            query = request.GET['query']
            data = client.venues.search(params={'query': query, 'intent': 'global'})
        elif request.method == "GET" and 'll' in request.GET:
            ll = request.GET['ll']
            data = client.venues.search(params={'ll': ll,})
        else:
            query = ""
            ll = ""
            data = {}
    except:
        query = ""
        ll = ""
        data = {}

    response = HttpResponse(json.dumps(data))

    #---begin--- for errors
    response["Access-Control-Allow-Origin"] = "localhost, *.ngrok.io"
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "localhost, *.ngrok.io"
    #---stop---

    return response
#---stop---


#---begin--- index page
def index(request):
    if request.user.is_anonymous():
        return render(request, 'welcome.html')
    else:
        return render(request, 'index.html')
#---stop---

def browse(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render(request, 'index.html')


def send_fama(request):
    if request.method == "POST":
        form = FamaForm(request.POST)
        if form.is_valid():
            personel = form.save(commit=False)
            personel.author = request.user
            personel.save()
    else:
        form = FamaForm()
    return HttpResponse('')


def list_fama(request):
    if request.method == "GET":
        place = request.GET["place"]
        data = []
        list = Fama.objects.filter(place=place)

        for i in list:
            data.append({
                "id": str(i.id),
                "title": i.title,
                "desc": i.desc,
                "date":{
                    "day": i.pub_date.day,
                    "month": i.pub_date.strftime("%B"),
                    "year": i.pub_date.year,
                    "hour": i.pub_date.strftime("%H"),
                    "minute": i.pub_date.strftime("%M"),
                },
                "author": i.author.username
            })

        response = HttpResponse(json.dumps(data))

        #---begin--- for errors
        response["Access-Control-Allow-Origin"] = "localhost, *.ngrok.io"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "localhost, *.ngrok.io"
        #---stop---

        return response
    else:
        return HttpResponse("")


def famasPage(request):
    if request.method == "GET":
        try:
            if request.GET["place_id"]:
                place_id = request.GET["place_id"]
            else:
                raise Http404
        except:
            raise Http404

        venue = client.venues(place_id)
        famas = Fama.objects.filter(place=place_id)

        return render(request, 'famasPage.html', {'famas': famas, 'venue': venue})


def thefamaPage(request):
    if request.method == "GET":
        try:
            if request.GET['id']:
                fama_id = request.GET['id']
            else:
                raise Http404
        except:
            raise Http404

        fama = get_object_or_404(Fama, id=fama_id)
        place_id = fama.place
        venue = client.venues(place_id)

        return render(request, 'thefamaPage.html', {'fama': fama, 'venue': venue})


def customLogin(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return login(request, **kwargs)


def register(request):
    if request.user.is_anonymous():
        user_form = UserForm(request.POST or None)
        reporter_form = ReporterForm(request.POST or None)
        if request.method == "POST":
            if user_form.is_valid() and reporter_form.is_valid():
                user = user_form.save()
                user.save()

                reporter = reporter_form.save(commit=False)
                reporter.user = user
                reporter.save()
                return HttpResponseRedirect('/login')
        return render(request, 'registration/register.html', {'userForm': user_form, 'reporterForm': reporter_form})
    else:
        return HttpResponseRedirect('/')

def registerControl(request):
    data = {}
    if request.method == "GET":
        if request.GET['email']:
            email = request.GET['email']
            if email and User.objects.filter(email=email):
                data['email'] = 'available'
            else:
                data['email'] = ''

        if request.GET['username']:
            username = request.GET['username']
            if username and User.objects.filter(username=username):
                data['username'] = 'available'
            else:
                data['username'] = ''

        response = HttpResponse(json.dumps(data))

        #---begin--- for errors
        response["Access-Control-Allow-Origin"] = "localhost, *.ngrok.io"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "localhost, *.ngrok.io"
        #---stop---

        return response


def ReporterProfilePage(request):
    if request.method == "GET":
        try:
            if request.GET['id']:
                user_id = int(request.GET['id'])
        except:
            user_id = 0

        if Reporter.objects.filter(user__id=user_id):
            reporter = Reporter.objects.get(user__id=user_id)

            return render(request, 'profile/reporter_page.html', {'reporter': reporter, 'famas': reporter.get_famas})
        else:
            raise Http404


def SettingsFama(request):
    if request.user.is_authenticated():
        return render(request, 'settings/main.html', {'user':request.user})
    else:
        return HttpResponseRedirect('/login')


def ChangeEmailPage(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)

        if request.method == "POST":
            form = ChangeEmailForm(request.POST)
            if form.is_valid():
                if user.email == form.cleaned_data['old_email']:
                    user.email = form.cleaned_data['new_email']
                    user.save()
                    return HttpResponseRedirect('done')
        else:
            form = ChangeEmailForm()

        return render_to_response('settings/change_email.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def ChangeEmailDonePage(request):
    if request.user.is_authenticated():
        return render(request, 'settings/change_email_done.html')
    else:
        return HttpResponseRedirect('/login')


def CustomPasswordChange(request, **kwargs):
    if request.user.is_authenticated():
        return MyPasswordChangeForm(request, **kwargs)
    else:
        return HttpResponseRedirect('/login')


def LastMinuteFamas(request):
    famas = Fama.objects.all()

    return render(request, 'last_minute_famas.html', {'famas': famas})


def SendTicketPage(request):
    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("done")
    else:
        form = TicketForm()

    return render(request, 'send_ticket.html', {'form': form})

def SendTicketDonePage(request):
    return render(request, 'send_ticket_done.html')


def FamasOnTheNearPage(request):
    return HttpResponseRedirect('/')


def ChangeProfilePicturePage(request):
    if request.user.is_authenticated():
        reporter = Reporter.objects.get(user__username=request.user.username)

        if request.method == "POST":
            form = ChangeProfilePictureForm(request.POST, request.FILES)

            if form.is_valid():
                reporter.profile_picture = request.FILES['profile_picture']
                reporter.save()
        else:
            form = ChangeProfilePictureForm()

        return render(request,'settings/change_profile_picture.html', {'form': form, 'reporter':reporter})
    else:
        return HttpResponseRedirect('/login')