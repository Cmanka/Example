from django import forms


class Proc1Form(forms.Form):
    hall_name = forms.ChoiceField()
