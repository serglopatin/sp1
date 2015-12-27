from urlparse import urljoin
from os import path
from saml2 import saml
import saml2

from common_settings import *

def get_saml_config(ROOT_URL, BASEDIR):

	return {
		# full path to the xmlsec1 binary programm
		'xmlsec_binary': '/usr/bin/xmlsec1',

		# your entity id, usually your subdomain plus the url to the metadata view
		'entityid': urljoin(ROOT_URL,"/saml2/metadata/"),

		# directory with attribute mapping
		'attribute_map_dir': path.join(BASEDIR, ATTRIB_MAP_DIR_PATH),

		# this block states what services we provide
		'service': {
			# we are just a lonely SP
			'sp': {
				#fixme!
				'allow_unsolicited':True,

				"logout_requests_signed": "true",
				"authn_requests_signed": "true",
				'name': 'Federated Django sample SP',
				'name_id_format': saml.NAMEID_FORMAT_TRANSIENT,
				'endpoints': {
					# url and binding to the assetion consumer service view
					# do not change the binding or service name
					'assertion_consumer_service': [
						(urljoin(ROOT_URL,"/saml2/acs/"),
						 saml2.BINDING_HTTP_POST),
					],
					# url and binding to the single logout service view
					# do not change the binding or service name
					'single_logout_service': [
						(urljoin(ROOT_URL,"/saml2/ls/"),
						 saml2.BINDING_HTTP_REDIRECT),
						(urljoin(ROOT_URL, '/saml2/ls/post/'),
						 saml2.BINDING_HTTP_POST),
					],
				},

			},
		},

		# where the remote metadata is stored
		'metadata': {
			'local': [path.join(BASEDIR, IDP_META_PATH)],
		},

		# set to 1 to output debugging information
		'debug': 1,
		'timeslack':5000,
		'accepted_time_diff':5000,

		# certificate
		'key_file': path.join(BASEDIR, SP_KEY_PATH),  # private part
		'cert_file': path.join(BASEDIR, SP_CRT_PATH),  # public part

		'valid_for': 24,  # how long is our metadata valid
	}
