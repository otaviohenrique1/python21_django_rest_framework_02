def cpf_invalido(cpf: str):
    return len(cpf) != 11

def nome_invalido(nome: str):
    return not nome.isalpha()

def celular_invalido(celular: str):
    return len(celular) != 13
