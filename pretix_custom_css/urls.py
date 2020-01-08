from django.conf.urls import url

from .views import SettingsView

urlpatterns = [
    url(
        r"^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/pretix_custom_css/settings",
        SettingsView.as_view(),
        name="settings",
    ),
]
