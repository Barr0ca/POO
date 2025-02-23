def fun():
    raise ConnectionError
try:
    fun()
except ConnectionError as exc:
    # raise #Para subir a mesma exceção "ConnectionError"
    exc.add_note("Provável error de tamanho de disco atingido") #Emitido uma nota para o programador
    # raise 
    raise RuntimeError('Failed to open database') from exc #Para subir uma nova exceção "RuntimeError"
