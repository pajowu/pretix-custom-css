from django.urls import reverse
from pretix.control.views.event import EventSettingsFormView, EventSettingsViewMixin
from pretix.base.models.event import Event
from .forms import CustomCSSSettingsForm

from pretix.presale.style import regenerate_css
from django.contrib import messages


class SettingsView(EventSettingsViewMixin, EventSettingsFormView):
    model = Event
    permission = "can_change_settings"
    form_class = CustomCSSSettingsForm
    template_name = "pretix_custom_css/settings.html"

    def get_success_url(self, **kwargs):
        regenerate_css.apply_async(args=(self.request.event.pk,))
        messages.success(
            self.request,
            (
                "Your changes have been saved. Please note that it can "
                "take a short period of time until your changes become "
                "active."
            ),
        )

        return reverse(
            "plugins:pretix_custom_css:settings",
            kwargs={
                "organizer": self.request.event.organizer.slug,
                "event": self.request.event.slug,
            },
        )
