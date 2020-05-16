from django.utils.module_loading import autodiscover_modules
from .xadmin import site


def autodiscover():
    autodiscover_modules('xadmin', register_to=site)

default_app_config = 'django_xadmin.xadmin.apps.XadminConfig'


""""
加载settings.INSTALL_APPS
django.contrib.admin 
===> __init__.py 
===> default_app_config = 'django.contrib.admin.apps.AdminConfig'
===> AdminConfig.ready ==>      def ready(self):
                                    super().ready()
                                    self.module.autodiscover()
===> # 初始化，调用每个模块admin.py
def autodiscover():
    autodiscover_modules('admin', register_to=site)
                                                                  
"""