from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    page_id = models.TextField(max_length=20, unique=True)
    name = models.TextField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lead(models.Model):
    leadgen_id = models.TextField(max_length=20)
    first_name = models.TextField(max_length=20, null=True, blank=True)
    last_name = models.TextField(max_length=20, null=True, blank=True)
    phone_number = models.TextField(max_length=20, null=True, blank=True)
    email = models.TextField(max_length=20, null=True, blank=True)
    extras = models.TextField(max_length=255, null=True, blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.page.name + "-" + self.first_name

    def create_from_fb_lead(self, fb_lead, page):
        keyword = ('first_name', 'last_name', 'phone_number', 'email',)
        list_values = fb_lead['field_data']
        data = {}
        extras = {}
        for entry in list_values:
            if entry['name'] in keyword:
                data[entry['name']] = entry['values']
            else:
                extras[entry['name']] = entry['values']

        self.leadgen_id = fb_lead.get('id')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.phone_number = data.get('phone_number')
        self.email = data.get('email')
        self.extras = str(extras)
        self.page = page
        self.save()


class PageTeam(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.page.name + "-" + self.user.first_name
