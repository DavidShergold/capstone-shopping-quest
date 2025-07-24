# Local development settings with PostgreSQL
# Copy this to local_settings.py and modify for your local PostgreSQL setup

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shoppingquest_dev',
        'USER': 'postgres',  # Default PostgreSQL user
        'PASSWORD': 'your_password_here',  # Set during PostgreSQL installation
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Override for local development
DEBUG = True
