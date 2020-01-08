from django import forms
from django.utils.translation import ugettext_lazy as _
from pretix.base.forms import SettingsForm


class CustomCSSSettingsForm(SettingsForm):
    custom_css_code = forms.CharField(label=_("Custom CSS"), widget=forms.Textarea)
