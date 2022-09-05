from xml.dom.minidom import Attr
from .models import *
from django import forms
# from bootstrap_datepicker_plus.widgets import TimePickerInput

# class coursesform(forms.ModelForm):
#     class Meta:
#         model = courses
#         fields = "__all__"
#         widgets={'starttime' : TimePickerInput(),
#         }


class coursesform(forms.ModelForm):
    class Meta:
        model = loans
        fields = "__all__"
        # exclude = ['title']

class Loginform(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"
            }
        )
    )