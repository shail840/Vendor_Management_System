from django.apps import AppConfig


class VendorSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VMSapi'

    def ready(self):
        import VMSapi.signals
