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

def my_saml_logout(request, config_loader_path=None):

	try:
		if request.user.is_authenticated():

			return djangosaml2_logout(request, config_loader_path)
		else:
			return redirect('home')

	except:
		logger.debug('ERROR djangosaml2_logout')
		django_logout(request)
		return redirect('home')

