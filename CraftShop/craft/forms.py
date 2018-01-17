from django import forms
from .models import Craft
class NewsLetterForm(forms.Form):
    your_name=forms.CharField(label='First Name',max_length=30)
    email=forms.EmailField(label='Email')

class NewCraftForm(forms.ModelForm):
    class Meta:
        model=Craft
        exclude=['artist','post_date']
        widgets={
        'category':forms.CheckboxSelectMultiple(),
        }
