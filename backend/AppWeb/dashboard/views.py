from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models
import json
from facebookads.adobjects.lead import Lead
from facebookads.api import FacebookAdsApi


def home(request):
    return render(request, 'dashboard/home.html', locals())


@login_required
def dashboard(request):
    return render(request, 'dashboard/.html', locals())


@csrf_exempt
def webhook(request):
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.body)

    challenge = request.GET.get("hub.challenge", "")
    token = request.GET.get("hub.verify_token", "")
    mode = request.GET.get('hub.mode', "")
    msg = 'you are an error!'
    if token == 'abc1234':
        return HttpResponse(challenge)

    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        entry = body['entry'][0]['changes'][0]['value']

        ad_id = entry['ad_id']
        form_id = entry['form_id']
        leadgen_id = entry['leadgen_id']
        created_time = entry['created_time']
        page_id = entry['page_id']
        adgroup_id = entry['adgroup_id']

        # TODO FB recognize LeadGen
        my_app_id = '490907924631684'
        my_app_secret = '4f2cf3ce3047c7c6893bd765915c2178'
        my_access_token = 'EAAGZBemh3EIQBAG3ReLbWCZAGLB7mH5XRfwGXpqZCUU78FLvhRIxJXCSMrZATkGinnJfRwWkZAlZB5bp4OvQyAJ1Ou7ks2udFL7cPNgZAD47VEwm8ARXeZAM1NO8ZC1LaZBtExX76wRZCV2XezXibMvLcyKdtGLbavMJuQZD'

        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

        fields = [
        ]

        params = {
        }

        page = models.Page.objects.get(page_id=page_id)
        fb_lead = Lead(leadgen_id).api_get(fields=fields, params=params, )
        lead = models.Lead.create_from_fb_lead(fb_lead, page)
        msg = 'lead saved!'
    except Exception as e:
        print('%s (%s)' % (str(e), type(e)))

        msg = 'lead did not saved :('

    return HttpResponse(msg)
