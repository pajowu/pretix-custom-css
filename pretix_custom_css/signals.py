from django.dispatch import receiver
from django.urls import resolve, reverse
from django.utils.translation import ugettext_lazy as _
from pretix.presale.signals import html_head as html_head_presale
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


@receiver(html_head_presale, dispatch_uid="custom_css_html_head_presale")
def html_head_presale(sender, request=None, **kwargs):
    if sender.settings.custom_css_code:
        return "<style>" + sender.settings.custom_css_code + "</style>"
    else:
        return ""
