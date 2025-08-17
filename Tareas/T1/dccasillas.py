
class DCCasillas:

    def __init__(self, usuario:str, config:str) -> None:
        self.usuario = usuario
        self.puntaje = 0
        self.tablero_actual = None
        self.tableros = config

    def abrir_tablero(self, num_tablero:int) -> None:
        pass

    def guardar_estado(self) -> bool: 
        pass

    def recuperar_estado(self) -> bool:
        pass
        
