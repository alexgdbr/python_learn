"""
Módulo centralizado de validações do sistema.
"""

from datetime import datetime
import re

def validar_cpf(cpf: str) -> bool:
    """Valida se o CPF contém apenas dígitos e possui o número correto de caracteres."""
    # Limpa caracteres não numéricos
    cpf_limpo = re.sub(r'\D', '', cpf)
    
    # Verifica tamanho e se não são todos os dígitos iguais (ex: 11111111111)
    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        return False
        
    # Cálculo do 1º dígito verificador
    soma = sum(int(cpf_limpo[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = resto if resto < 10 else 0
    if digito1 != int(cpf_limpo[9]):
        return False

    # Cálculo do 2º dígito verificador
    soma = sum(int(cpf_limpo[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = resto if resto < 10 else 0
    if digito2 != int(cpf_limpo[10]):
        return False

    return True


def validar_emailinst(email: str) -> bool:
    """Valida se o e-mail pertence ao domínio institucional @saude.gov.br."""
    email_limpo = email.strip().lower()
    return email_limpo.endswith("@saude.gov.br") and len(email_limpo) > 13


def validar_data(data: str) -> bool:
    """Valida se a data está no formato dd/mm/aaaa e se é uma data real."""
    try:
        datetime.strptime(data.strip(), "%d/%m/%Y")
        return True
    except ValueError:
        return False