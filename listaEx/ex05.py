class NomeInvalidoError(Exception):
    pass
class IdadeInvalidaError(Exception):
    pass
class EmailInvalidoError(Exception):
    pass

class Usuario:
    nome = str
    idade = int
    email = str

    def __init__(self, nome, idade, email):
        if len(nome) < 3:
            raise NomeInvalidoError('Nome deve conter pelo menos 3 caracteres.')
        elif idade <= 18:
            raise IdadeInvalidaError('Idade deve ser maior que 18 anos.')
        elif '@' not in email:
            raise EmailInvalidoError('O campo E-mail deve conter o caracter [@].')
        return print(f'Usuário: {nome}\nIdade: {idade}\nEmail: {email}')
    
try:
    usuario01 = Usuario('Ian', 19, 'ian@gmail.com')
except (NomeInvalidoError, IdadeInvalidaError, EmailInvalidoError) as exc:
    print(exc)