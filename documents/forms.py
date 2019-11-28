from django import forms

from .models import files,Binding


class FileForm(forms.ModelForm):
   # your_name = forms.CharField(label='enter title for file', max_length=100)
    class Meta:
        model = files
     

        fields = ('file','title','pages','user_id')
        labels = {'title': 'enter title for file',}
        error_css_class = 'error'
         
         
    class Media:
        css = {
            'all': ('css/layout.css',),
            
        }
class BindingForm(forms.ModelForm):
    class Meta:
        model = Binding
        fields = ('image', )
