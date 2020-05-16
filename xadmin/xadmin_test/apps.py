from django.apps import AppConfig


class XadminConfig(AppConfig):
    name = 'xadmin'

    def ready(self):
        super().ready()
        self.module.autodiscover()