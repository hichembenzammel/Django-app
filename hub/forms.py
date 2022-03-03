from django import forms

from .models import Student

# 2eme methode de formulaire
class StudentForm(forms.Form):
    first_name=forms.CharField(
        label='Prenom',
        max_length=50
    )
    last_name=forms.CharField(
        label='Nom',
    )
    email=forms.EmailField(
        label='E-mail'
    )


# 3 eme methode de formulaire
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" #ou ['last_name','first_name','email']
        #exclude=[] pour n'afficher pas des attribut a ajouter au formulaire
