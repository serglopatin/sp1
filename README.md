# sp1 - sample django service provider

This is basic django website based on djangosaml2 module to test Shibboleth SSO. It contains only single page with login button.

##Installation
1. Clone sp1:
  ```
cd ~
git clone https://github.com/serglopatin/sp1.git
```

2. Generate certificate and key:
  ```
cd ~/sp1/sp1/
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout sp1_key.key -out sp1_cert.pem
```

3. If neccessary customize host name (sp1.localhost), key paths (key='sp1_key.key', crt='sp1_cert.pem') and idp metadata path ('idp_metadata.xml') in files:
  ```
settings.py
saml_config.py
```

4. Deploy SP as regular django website.

5. Logs will be written to sp1/django_request.log - you need to give appropriate permissions to it.

##How it works
1. Go to sp1.localhost and click 'login'
2. You will be redirected to idp.localhost, where you should enter login/password
3. IDP redirects you back to SP, where your username is displayed

For more details on how to deploy Shibboleth IDP and Django SP refer to [this post](http://codeinpython.blogspot.com/2015/11/how-to-setup-shibboleth-identity.html).
