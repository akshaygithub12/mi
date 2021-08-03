from django.apps import AppConfig


class SalesConfig(AppConfig):
    name = 'sales'

    def ready(Self):
        import sales.signals
