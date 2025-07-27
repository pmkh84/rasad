from django import forms
from .models import PresenceRecord

class form_type(forms.Form):
    forms_date = forms.CharField()
    type_choice = forms.ChoiceField(choices=[
        ('نماز', 'نماز'),
        ('برنامه ویژه', ' برنامه ویژه'),
        ('هییت','هییت'),
        ('حلقه9','9حلقه'),
        ('حلقه10','10حلقه'),
        ('حلقه11','11حلقه'),
        ('حلقه12','12حلقه'),
        ('حلقه13','حلقه13'),
        ('حلقه14','14حلقه'),
        ('حلقه15','15حلقه'),
        ('حلقه16','16حلقه'),
        ('حلقه17','17حلقه'),
        ('حلقه18','18حلقه'),

    ])

class presance_form(forms.ModelForm):
    class Meta:
        model = PresenceRecord
        fields = ['present', 'member']
        widgets = {
            'member': forms.HiddenInput()
        }
class login(forms.Form):
    name = forms.CharField(label = 'نام و نام خانوادگی ')
    pass_word = forms.CharField(label = 'رمز عبور')      