from django.apps import AppConfig


class AggregatorConfig(AppConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'
    name = 'aggregator'
