from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'dashboard/home.html', locals())


@login_required
def dashboard(request):
    return render(request, 'dashboard/.html', locals())


def webhook(request):
    print(request.POST)
    challenge = request.POST.get("hub_challenge", "")
    print(challenge)
    token = request.POST.get("hub_verify_token", "")
    print(token)
    if token == 'abc1234':
        return HttpResponse(challenge)
    return HttpResponse('you are an error!')
