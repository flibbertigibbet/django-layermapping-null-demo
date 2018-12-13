# This is a test settings file for use with the Django test suite.
#
# https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/
#
# The different databases that Django supports behave differently in certain
# situations, so it is recommended to run the test suite against as many
# database backends as possible.  You may want to create a separate settings
# file for each of the backends you test against.

# Cannot set via environment variables from .env because tox loses them

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'layermapping',
        'USER': 'layermapping',
        'PASSWORD': 'layermapping',
        'HOST': 'database.service.layermapping.internal',
        'PORT': 5444
    },
    'other': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'layermapping',
        'USER': 'layermapping',
        'PASSWORD': 'layermapping',
        'HOST': 'database.service.layermapping.internal',
        'PORT': 5444
    },
}

SECRET_KEY = 'JUST_WORK_ALREADY'
