from .default import *

#
# Debug or not
#
DEBUG = False
VERSION = 1.0


# Only allow token authentication in production
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = ('rest_framework.authentication.TokenAuthentication')