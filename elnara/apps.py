from django.apps import AppConfig


class ElnaraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #### added new as i was getting error
    name = 'elnara'
