# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path

class Xadmin():

    _registry = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_sign"):
            cls._sign = super().__new__(cls, *args, **kwargs)
        return cls._sign

    def register(self, model, admin_class=None, **options):
        if admin_class is None:
            admin_class = admin.ModelAdmin
        self._registry[model] =  admin_class(model, self)

    @property
    def urls(self):
        return self.get_urls(), None , None

    def get_urls(self):
        temp = []
        for model, model_admin in self._registry.items():
            temp.append(path("{0}/{1}/".format(model._meta.app_label, model._meta.model_name),model_admin.urls))

        print(temp)
        return temp

site = Xadmin()

