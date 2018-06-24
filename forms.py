from django.contrib.auth.models import User
from django import forms
from django.core.validators import  validate_email
from LitTalkIndex.models import  AddHindiPoem

class userform(forms.ModelForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'},
                                                    ), required=True,max_length=40)
    EmailId = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' email id'},
                                                      ), required=True, max_length=40)

    first_name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'},
                                                      ), required=True, max_length=40)

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'},
                                                      ), required=True, max_length=40)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'},
                                                      ), required=True, max_length=10)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 're-enter the passsword'},
                                                      ), required=True, max_length=10)
    class Meta():
        model=User
        fields=['username', 'EmailId',  'first_name', 'last_name', 'password']

    def clean_username(self):
        user=self.cleaned_data['username']
        try:
            match = User.objects.get(username = user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('username alrady exit')
    def  clean_email(self):
        email=self.cleaned_data['email']
        try:
            mt= validate_email(email)
        except:
            return  forms.ValidateError('ema is not correct')
        return  email
    def claen_confirm_password(self):
        pas=self.cleaned_data['password']
        c_pass = self.cleaned_data['confirm_password']
        min_len=8
        if pas and  c_pass:
            if pas!=c_pass:
                raise forms.ValidationError(" password and confirm password dont match")
            else:
                if(len(pas)< min_len):
                    raise forms.ValidationError("password length atleat %d in length")
                if pas.isdigit():
                     raise forms.ValidationError("password cant be only nueric value")
                if pas.isalpha():
                  raise  forms.ValidationError("passwor cant be only alpha ...")






class AddHindiPoemForm(forms.ModelForm):

    Authoname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'},
                                                    ), required=True,max_length=40)
    Type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hindi/English'},
                                                       ), required=True, max_length=40)
    Title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'},
                                                       ), required=True, max_length=40)
    Content= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'},
                                                       ), required=True, max_length=40)
    class Meta:
        model = AddHindiPoem
        fields = "__all__"







