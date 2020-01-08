from django.dispatch import receiver
from django.urls import resolve, reverse
from django.utils.translation import ugettext_lazy as _
from pretix.presale.signals import sass_postamble
from pretix.control.signals import nav_event_settings


@receiver(nav_event_settings, dispatch_uid="custom_css_settings")
def custom_css_settings(sender, request, **kwargs):
    url = resolve(request.path_info)
    return [
        {
            "label": _("Custom CSS"),
            "url": reverse(
                "plugins:pretix_custom_css:settings",
                kwargs={
                    "event": request.event.slug,
                    "organizer": request.organizer.slug,
                },
            ),
            "active": url.namespace == "plugins:pretix_custom_css"
            and url.url_name == "settings",
        }
    ]


@receiver(sass_postamble, dispatch_uid="custom_css_sass_postamble")
def custom_css_sass_postamble(sender, filename=None, **kwargs):
    if sender.settings.custom_css_code:
        return sender.settings.custom_css_code
    else:
        return ""
