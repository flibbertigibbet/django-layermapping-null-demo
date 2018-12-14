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
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': '/usr/src/test_layermapping.db',
    },
    'other': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': '/usr/src/test_other.db',
    }
}


SPATIALITE_LIBRARY_PATH = 'mod_spatialite.so'

SECRET_KEY = 'WHY_DO_TESTS_NEED_A_SECRET_KEY'

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
