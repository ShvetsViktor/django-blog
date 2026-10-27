from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configures the Blog application.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'