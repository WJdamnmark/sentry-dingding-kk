# coding: utf-8

from django import forms


class DingDingOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token'
    )
    secret_key = forms.CharField(
        max_length=255,
        help_text='DingTalk robot secret key'
    )
