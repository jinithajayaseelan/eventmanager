from django import forms

class NameForm(forms.Form):
    class Meta:
        your_name= forms.CharField(max_length=100)
        def __str__(self):
            return self.title