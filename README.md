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

3. Customize necessary settings by editing file **sp1/common_settings.py** (hostname, key path, log path, sqlite db path, etc)

4. Create virtualenv
  ```
cd ~
virtualenv sp1_env
source sp1_env/bin/activate
pip install -r ~/sp1/requirements.txt
```

5. Migrate database:
  ```
cd ~/sp1
python manage.py migrate
```

6. Deploy SP as regular django website (for example, using uwsgi+nginx).

7. Give write permissions to **sp1/www_data** directory (used for sqlite db and django_request.log) for your webserver user.

##How it works
1. Go to sp1.localhost and click 'login'
2. You will be redirected to idp.localhost, where you should enter login/password
3. IDP redirects you back to SP, where your username is displayed

For more details on how to deploy Shibboleth IDP and Django SP refer to [this post](http://codeinpython.blogspot.com/2015/11/how-to-setup-shibboleth-identity.html).
