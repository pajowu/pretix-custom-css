from django.utils.translation import ugettext_lazy
try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    name = 'pretix_custom_css'
    verbose_name = 'Pretix Custom CSS'

    class PretixPluginMeta:
        name = ugettext_lazy('Pretix Custom CSS')
        author = 'Karl Engelhardt'
        description = ugettext_lazy('Include Custom CSS code in all pretix pages')
        visible = True
        version = '1.1.1'
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_custom_css.PluginApp'
