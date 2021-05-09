from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar('maldrax@gmail.com',
                                'delith@gmail.com',
                                'Curso Python Pro',
                                'Turmas abertas para o curso.'
                                )
    assert 'maldrax@gmail.com' in resultado
