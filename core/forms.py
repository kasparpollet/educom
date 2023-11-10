from django import forms

from core.models import Person

# class PersonForm(forms.ModelForm):
#     # full_name = forms.CharField()
#     # birthdate = forms.DateField()

#     class Meta:
#         model = Person 
#         fields = ['full_name','birthdate']

#         # def __init__(self, *args, **kwargs):
#         #    super().__init__(*args, **kwargs)
#         #    self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
#         #    self.fields['birthdate'].widget.attrs.update({'class':'form-control'})


class PersonForm(forms.Form):
    full_name = forms.CharField(label="Full name", max_length=100)
    birthdate = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'