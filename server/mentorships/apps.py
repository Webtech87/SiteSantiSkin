from django.apps import AppConfig


class MentorshipsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mentorships'

    def ready(self):
        import mentorships.signals
