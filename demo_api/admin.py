
from django.contrib.admin import AdminSite
from django.http import HttpResponseRedirect

class CustomAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        return HttpResponseRedirect('/api/v1/')

admin_site = CustomAdminSite()