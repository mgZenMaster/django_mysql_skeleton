from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        self.declared_fields['username'].widget.attrs["class"] = "form-control"
        self.declared_fields['username'].widget.attrs["placeholder"] = "Username"
        self.declared_fields['password'].widget.attrs["class"] = "form-control"
        self.declared_fields['password'].widget.attrs["placeholder"] = "Password"

        super().__init__(*args, **kwargs)


class UserForm(ModelForm):

    class Meta:

        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Button('cancel', 'Cancel',
                                     css_class="btn-secondary",
                                     onclick="window.location='/'"))
