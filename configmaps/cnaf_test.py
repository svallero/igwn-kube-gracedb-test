# Settings for a test/dev GraceDB instance running in a container
from .base import *

CONFIG_NAME = "TEST"
# Send out alerts
SEND_XMPP_ALERTS = True
SEND_PHONE_ALERTS = False
SEND_EMAIL_ALERTS = False

# Debug settings
DEBUG = True

# Override EMBB email address
# TP (8 Aug 2017): not sure why?
EMBB_MAIL_ADDRESS = 'gracedb@{fqdn}'.format(fqdn=SERVER_FQDN)

# Add middleware
debug_middleware = 'debug_toolbar.middleware.DebugToolbarMiddleware'
MIDDLEWARE += [
    debug_middleware,
    #'silk.middleware.SilkyMiddleware',
    #'core.middleware.profiling.ProfileMiddleware',
    #'core.middleware.admin.AdminsOnlyMiddleware',
]

# Add to installed apps                                            
INSTALLED_APPS += [                                                
    'debug_toolbar',                                               
    #'silk'                                                        
]                                                                  
                                                                   
# Add testserver to ALLOWED_HOSTS                                  
ALLOWED_HOSTS += ['testserver']                                    
                                                                   
# Settings for django-silk profiler                                
SILKY_AUTHENTICATION = True                                        
SILKY_AUTHORISATION = True                                         
if 'silk' in INSTALLED_APPS:                                       
    # Needed to prevent RequestDataTooBig for files > 2.5 MB       
    # when silk is being used. This setting is typically used to   
    # prevent DOS attacks, so should not be changed in production. 
    DATA_UPLOAD_MAX_MEMORY_SIZE = 20*(1024**2)                     
                                                                   
# Tuple of IPs which are marked as internal, useful for debugging. 
# Tanner (5 Dec. 2017): DON'T CHANGE THIS! Django Debug Toolbar exposes          
# some headers which we want to keep hidden.  So to be safe, we only allow 
# it to be used through this server.  You need to configure a SOCKS proxy        
# on your local machine to use DJDT (see admin docs).              
INTERNAL_IPS = [                                                   
    INTERNAL_IP_ADDRESS,                                           
]                                                                  
                                                                   
# Adjust ADMINS for dev instances                                  
ADMINS = [                                                         
    ("Sara Vallero", "svallero@to.infn.it"),                       
]                                                                  
                                                                   
                                                                   
# Set up Sentry for error logging                                  
sentry_dsn = get_from_env('DJANGO_SENTRY_DSN', fail_if_not_found=False)          
if sentry_dsn is not None:                                         
    USE_SENTRY = True                                              
                                                                   
    # Set up Sentry                                                
    import sentry_sdk                                              
    from sentry_sdk.integrations.django import DjangoIntegration   
    sentry_sdk.init(                                               
        environment='test',           
        dsn=sentry_dsn,                                            
        integrations=[DjangoIntegration()]                         
    )                                                              
                                                                   
    # Turn off default admin error emails                          
    LOGGING['loggers']['django.request']['handlers'] = []          
                                                                   
# The default for this is False                                    
USE_SHIBBOLETH_LOGIN = False   

#CSRF_TRUSTED_ORIGINS = ['vm-131-154-161-31.cr.cnaf.infn.it:31511'] 
#CSRF_COOKIE_DOMAIN = '.cr.cnaf.infn.it'
#CSRF_TRUSTED_ORIGINS = ['gracedb-test']                   
#CSRF_COOKIE_DOMAIN = '.gracedb-test.svc.cluster.local'

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
