from crispy_forms.utils import render_crispy_form
from django_jinja import library
from jinja2 import pass_context


@library.global_function
@pass_context
def crispy(context, form):
    return render_crispy_form(form, context=context)
