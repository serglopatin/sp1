from urlparse import urljoin
from os import path
from saml2 import saml
import saml2


def get_saml_config(ROOT_URL, BASEDIR, key='sp1_key.key', crt='sp1_cert.pem'):

	return {
		# full path to the xmlsec1 binary programm
		'xmlsec_binary': '/usr/bin/xmlsec1',

		# your entity id, usually your subdomain plus the url to the metadata view
		'entityid': urljoin(ROOT_URL,"/saml2/metadata/"),

		# directory with attribute mapping
		'attribute_map_dir': path.join(BASEDIR, 'attribute-maps'),

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
						(urljoin(ROOT_URL, '/ls/post'),
						 saml2.BINDING_HTTP_POST),
					],
				},

				# attributes that this project need to identify a user
				#'required_attributes': ['uid'],
				#'required_attributes': ['uid'],

				# attributes that may be useful to have but not required
				#'optional_attributes': ['eduPersonAffiliation'],


			},
		},

		# where the remote metadata is stored
		'metadata': {
			'local': [path.join(BASEDIR, 'idp_metadata.xml')],
		},

		# set to 1 to output debugging information
		'debug': 1,
		'timeslack':5000,
		'accepted_time_diff':5000,


		# certificate
		'key_file': path.join(BASEDIR, key),  # private part
		'cert_file': path.join(BASEDIR, crt),  # public part

		# own metadata settings
		'contact_person': [
			{'given_name': 'Lorenzo',
			 'sur_name': 'Gil',
			 'company': 'Yaco Sistemas',
			 'email_address': 'lgs@yaco.es',
			 'contact_type': 'technical'},
			{'given_name': 'Angel',
			 'sur_name': 'Fernandez',
			 'company': 'Yaco Sistemas',
			 'email_address': 'angel@yaco.es',
			 'contact_type': 'administrative'},
		],
		# you can set multilanguage information here
		'organization': {
			'name': [('Yaco Sistemas', 'es'), ('Yaco Systems', 'en')],
			'display_name': [('Yaco', 'es'), ('Yaco', 'en')],
			'url': [('http://www.yaco.es', 'es'), ('http://www.yaco.com', 'en')],
		},
		'valid_for': 24,  # how long is our metadata valid
	}
