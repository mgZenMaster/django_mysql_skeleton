from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        self.declared_fields['username'].widget.attrs["class"] = "form-control"
        self.declared_fields['username'].widget.attrs["placeholder"] = "Username"
        self.declared_fields['password'].widget.attrs["class"] = "form-control"
        self.declared_fields['password'].widget.attrs["placeholder"] = "Password"

        super().__init__(*args, **kwargs)