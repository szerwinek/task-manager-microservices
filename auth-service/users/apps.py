from django.apps import AppConfig
import os


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        if os.environ.get("CREATE_SUPERUSER") == "true":
            from django.contrib.auth import get_user_model
            User = get_user_model()

            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="admin123"
                )
