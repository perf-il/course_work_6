from django import forms
from mail_sender.models import Customer, ContentEmail, SendSettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class CustomerForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class WriteEmailForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = ContentEmail
        exclude = ('created_by',)


class SendSettingsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = SendSettings
        exclude = ('status', 'created_by',)

