# -*- coding: utf-8 -*-
from xadmin.xadmin import site

from .models import Author
from django.shortcuts import HttpResponse
from django.urls import path

class AuthorXadmin:

    def __init__(self, model, admin_site):
        self.model = model
        self.admin_site = admin_site
        print(self.admin_site)

    def list_view(self,request):
        return HttpResponse("list view")

    def add_view(self,request):
        return HttpResponse("add view")

    def change_view(self,request, pk):
        return HttpResponse("change view")

    def delete_view(self,request, pk):
        return HttpResponse("delete view")

    @property
    def urls(self):
        temp = [
            path("", self.list_view),
            path("add/", self.add_view),
            path("<int:pk>/change/", self.change_view),
            path("<int:pk>/delete/", self.delete_view),
        ]
        return temp, None, None

site.register(Author, AuthorXadmin)

