from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create a new custom form #
class UserRegisterForm(UserCreationForm) :
	email = forms.EmailField()

	# Creating a user once validated #
	class Meta: # the meta gives a workspace, keeping the configuration #
		model = User
		fields = ['username', 'email', 'password1', 'password2']