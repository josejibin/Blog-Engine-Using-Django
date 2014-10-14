from django import forms 

class NewPostForm(forms.Form):
	title = forms.CharField()
	#pub_date = forms.DateTimeField()
	text = forms.CharField(widget=forms.Textarea())

class CommentForm(forms.Form):
	name = forms.CharField()
	comment = forms.CharField(widget = forms.Textarea(attrs={'size':20}))

class LoginForm(forms.Form):
	name = forms.CharField()
	password = forms.CharField()

class SignUpForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField()