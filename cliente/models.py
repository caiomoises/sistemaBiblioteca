from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator

# Create your models here.

def valida_CPF(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.')
    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 digitos.') 

    invalid_cpfs = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555',
                    '66666666666', '77777777777', '88888888888', '99999999999']

    if value in invalid_cpfs:
        raise ValidationError('CPF inválido.')
    
    total = 0
    for i in range(9):
        total += int(value[i]) * (10 - i)

    resto = total % 11

    if resto < 2:
        digito_esperado = 0
    else:
        digito_esperado = 11 - resto

    if int(value[9]) != digito_esperado:
        raise ValidationError('CPF inválido.')

    total = 0
    for i in range(10):
        total += int(value[i]) * (11 - i)

    resto = total % 11

    if resto < 2:
        digito_esperado = 0
    else:
        digito_esperado = 11 - resto

    if int(value[10]) != digito_esperado:
        raise ValidationError('CPF inválido.')

def valida_contato(value):
    if not any(char.isdigit() for char in value):
        EmailValidator()(value)
    else:
        if not(9 <= len(value) <= 12 and value.isdigit()):
            raise ValidationError('Número de celular inválido.')

class cliente(models.Model):
    Nome = models.CharField(max_length=50, blank=False)
    CPF = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r'^\d{11}$', 'CPF deve conter apenas números.'), valida_CPF])
    Contato = models.CharField(max_length=50, null=True, blank=False, validators=[valida_contato])
    Logradouro = models.CharField(max_length=60, null=True, blank=False)

    def __str__(self) -> str:
        return self.Nome
