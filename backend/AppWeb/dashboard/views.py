from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'dashboard/home.html', locals())


@login_required
def dashboard(request):
    return render(request, 'dashboard/.html', locals())


@csrf_exempt
def webhook(request):
    print(request.GET)
    print(request.POST)
    challenge = request.GET.get("hub.challenge", "")
    token = request.GET.get("hub.verify_token", "")
    mode = request.GET.get('hub.mode', "")
    if token == 'abc1234':
        return HttpResponse(challenge)

    return HttpResponse("%s %s" % (request.method, request.body))
