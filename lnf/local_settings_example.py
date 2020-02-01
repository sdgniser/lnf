# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'an1vt^%sg9ro+-65cc^2a1j(p0e9brg6=rt9szxn#s^iy3)7(m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lnf',
        'USER': 'ayush',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Deployment checklist
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = 'DENY'
