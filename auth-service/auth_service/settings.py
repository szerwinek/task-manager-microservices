"""
Django settings for auth_service project.
"""

from pathlib import Path
import os

# --------------------------------------------------
# Paths
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------------------------------------
# Security
# --------------------------------------------------
SECRET_KEY = 'django-insecure--@%@^&$_y0f7d7_j5$s1jm8czd(*l*c0!%oji9k4=10&ype_8q'

# UWAGA:
# Lokalnie True, w Cloud Run nadal działa (projekt zaliczeniowy)
DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".run.app",
]

# 🔐 CSRF – WYMAGANE DLA CLOUD RUN
CSRF_TRUSTED_ORIGINS = [
    "https://auth-service-468382717388.europe-central2.run.app",
    "https://*.run.app",
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


# --------------------------------------------------
# Applications
# --------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'users',
]


# --------------------------------------------------
# Middleware
# --------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --------------------------------------------------
# URLs / WSGI
# --------------------------------------------------
ROOT_URLCONF = 'auth_service.urls'

WSGI_APPLICATION = 'auth_service.wsgi.application'


# --------------------------------------------------
# Templates
# --------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# --------------------------------------------------
# Database (SQLite – demo / zaliczenie)
# --------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --------------------------------------------------
# Password validation
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --------------------------------------------------
# Internationalization
# --------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --------------------------------------------------
# Static files
# --------------------------------------------------
STATIC_URL = 'static/'


# --------------------------------------------------
# Default PK
# --------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==================================================
# AUTOMATYCZNE TWORZENIE ADMINA (CLOUD RUN / DEMO)
# ==================================================
if os.environ.get("CREATE_SUPERUSER") == "true":
    from django.contrib.auth import get_user_model
    User = get_user_model()

    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="admin123"
        )

