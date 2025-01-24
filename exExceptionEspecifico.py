class MinhaExcecao(Exception):
    pass

def fun():
    raise MinhaExcecao('Não conectou')
try:
    fun()
except Exception as exc: #Sempre vai capturar o "Exception"
    exc.add_note("Provável error de tamanho de disco atingido") #Emitido uma nota para o programador
    raise RuntimeError('Failed to open database') from exc #Para subir uma nova exceção "RuntimeError"
