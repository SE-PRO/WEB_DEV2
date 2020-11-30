from django.forms import ModelForm
from .models import *
 
class CreateInForum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
       # widgets = {
        #    '__all__': form.TextInput(attrs={'class': 'mycssclass'}),
       # }
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"