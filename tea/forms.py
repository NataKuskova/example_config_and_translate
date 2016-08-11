from django import forms
from tea.models import *


class PhoneWidget(forms.MultiWidget):

    def __init__(self, code_l, n_l, attrs=None, *args):
        widgets = [forms.TextInput(attrs={'size':code_l, 'maxlength': code_l}),
                   forms.TextInput(attrs={'size': n_l, 'maxlength': n_l}),]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        return ['', '']

    def format_output(self, rendered_widgets):
        return '+38 (' + rendered_widgets[0] + ')' + rendered_widgets[1]


class PhoneField(forms.MultiValueField):
    def __init__(self, code_l, n_l, *args):
        list_fields = [forms.CharField(), forms.CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_l, n_l), *args)

    def compress(self, values):
        return '+38' + '(' + values[0] + ')' + values[1]

"""
class CreateUserForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    address = forms.CharField(max_length=100)
    phone = PhoneField(3, 7)
"""


class CreateUserForm(forms.ModelForm):
    phone = PhoneField(3, 7)

    class Meta:
        model = Buyer
        fields = ['name', 'surname', 'email', 'address', 'phone']

