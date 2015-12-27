from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from djangosaml2.views import logout as djangosaml2_logout

import logging
logger = logging.getLogger('sp1')

def view_profile(request):

	return render(request, 'sp1/profile.html',
				  {"user":request.user}
							  )

