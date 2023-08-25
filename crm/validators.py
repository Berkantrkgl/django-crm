from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _




def RegexValidator(value):
    if len(str(value)) != 11:
        raise ValidationError("Invalid Tc no!")