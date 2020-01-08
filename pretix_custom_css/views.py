from django.urls import reverse
from pretix.control.views.event import EventSettingsFormView, EventSettingsViewMixin
from pretix.base.models.event import Event
from .forms import CustomCSSSettingsForm


class SettingsView(EventSettingsViewMixin, EventSettingsFormView):
    model = Event
    permission = "can_change_settings"
    form_class = CustomCSSSettingsForm
    template_name = "pretix_custom_css/settings.html"

    def get_success_url(self, **kwargs):
        return reverse(
            "plugins:pretix_custom_css:settings",
            kwargs={
                "organizer": self.request.event.organizer.slug,
                "event": self.request.event.slug,
            },
        )
