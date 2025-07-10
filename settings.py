
import os
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Application definition
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',  # Add CORS headers to the installed apps
    'listings',  # Add listings app
    'drf_yasg',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',  # Add CORS middleware
    ...
]

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Specify your allowed origins
]

# Database configuration using environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),  # Database name
        'USER': env('DB_USER'),  # Database user
        'PASSWORD': env('DB_PASSWORD'),  # Database password
        'HOST': env('DB_HOST', default='127.0.0.1'),  # Database host
        'PORT': env('DB_PORT', default='3306'),  # Database port
    }
}
