from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# registering a user form #
def register(request):
	# verifier le type de requete pour ce formulaire #
	if request.method == 'POST' :
		# valider le formulaire
		form = UserCreationForm(request.POST)
		if form.is_valid():
			# formulaire valide, sauvegarder et afficher succes :
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for : {username}')
			# rederiger vers l'acceuil #
			return redirect('blog-home')
	else :
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form':form})
