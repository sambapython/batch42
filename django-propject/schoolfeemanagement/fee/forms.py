from django import forms
from models import School, OwnUser, PaymentHistory
from django.contrib.auth.models import User
class SignupForm(forms.Form):
	name = forms.CharField(max_length=100)
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)
	#username = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()
	phone = forms.CharField(max_length=100)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email","password"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class OwnUserForm(forms.ModelForm):
    class Meta:
        model = OwnUser
        fields = ["role1","name","phone","school","section"]


class SchoolForm(forms.ModelForm):
	class Meta:
		model = School
		fields = ["name","address"]
class PaymentHistoryForm(forms.ModelForm):
	class Meta:
		model = PaymentHistory
		fields = ['amount', 'student']
