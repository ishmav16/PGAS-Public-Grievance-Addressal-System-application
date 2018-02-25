from django import forms
from .models import Stock1
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
class StockForm(forms.ModelForm):
  class Meta:

      model=Stock1
      fields=['data','desc','lati','long','email1']


#class UserForm(forms.ModelForm):
 #   password = forms.CharField(widget=forms.PasswordInput)

  ##     model = User
    #    fields = ('username', 'email', 'password')
        # labels = {
        #     'username': 'Unique service no',

        # }

###
   #   model=User
    #  fields=['email','password']

#class UserProfileForm(forms.ModelForm):
 #   # phone_no = forms.CharField(widget=forms.)         need to complete it

  ###    fields = ('adhar_no',)


class NewForm(UserCreationForm):
    deptid = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ("username", "deptid", "password1", "password2")

    def save(self, commit=True):
        user = super(NewForm, self).save(commit=False)
        user.deptid = self.cleaned_data["deptid"]
        if commit:
            user.save()
        return user

