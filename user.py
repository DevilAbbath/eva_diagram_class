from survey import Encuesta
from answer import ListResp

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    def getCorreo(self) -> str:
        return self.__correo

    def setCorreo(self, correo: str) -> None:
        self.__correo = correo

    def getEdad(self) -> int:
        return self.__edad

    def setEdad(self, edad: int) -> None:
        self.__edad = edad

    def getRegion(self) -> int:
        return self.__region

    def setRegion(self, region: int) -> None:
        self.__region = region

    def contestarEncuesta(self, encuesta: Encuesta, respuestas: List[int]) -> None:
        listado = ListResp(self, respuestas)
        encuesta.agregarListResp(listado)
