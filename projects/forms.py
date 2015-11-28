from django import forms
from projects.models import Project


class UploadForm(forms.ModelForm):
    class Meta:
        # TODO: Make that if a field is not entered by the user, then add a
        # default value in the database, don't know if that is currently done
        # by default, in the models, need to check.
        model = Project
        fields = '__all__'
