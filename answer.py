from typing import List
from user import Usuario

class ListResp:
    def __init__(self, usuario: Usuario, respuestas: List[int]):
        self.__usuario = usuario
        self.__respuestas = respuestas

    def getUsuario(self) -> Usuario:
        return self.__usuario

    def getResp(self) -> List[int]:
        return self.__respuestas
