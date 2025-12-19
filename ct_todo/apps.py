from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ct_todo'

    def ready(self):
        import ct_todo.signals
