from django import forms
from .models import Comment
from django_recaptcha.widgets import ReCaptchaV2Checkbox 
from django_recaptcha.fields import ReCaptchaField

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'captcha')

class ContactForm(forms.Form): 
    name = forms.CharField(max_length=255)
    mailid = forms.EmailField(label='Email') 
    phone = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
