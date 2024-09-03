from typing import List, Dict
from question import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre: str, preguntas: List[Dict]):
        self.__nombre = nombre
        self.__preguntas = [Pregunta(**pregunta) for pregunta in preguntas]
        self.__listadosDeRespuestas = []

    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def mostrar(self) -> None:
        print(f"Nombre de la encuesta: {self.__nombre}")
        for pregunta in self.__preguntas:
            pregunta.mostrar()

    def agregarListadoRespuestas(self, listado: ListadoRespuestas) -> None:
        self.__listadosDeRespuestas.append(listado)

class EncLimitEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: List[Dict], edadMin: int, edadMax: int):
        super().__init__(nombre, preguntas)
        self.__edadMin = edadMin
        self.__edadMax = edadMax

    def getedadMin(self) -> int:
        return self.__edadMin

    def setedadMin(self, edadMin: int) -> None:
        self.__edadMin = edadMin

    def getedadMax(self) -> int:
        return self.__edadMax

    def setedadMax(self, edadMax: int) -> None:
        self.__edadMax = edadMax

    def agregarListadoRespuestas(self, listado: ListadoRespuestas) -> None:
        edad_usuario = listado.getUsuario().getEdad()
        if self.__edadMin <= edad_usuario <= self.__edadMax:
            super().agregarListadoRespuestas(listado)
        else:
            print("El usuario no cumple con el rango de edad.")

class EncLimitRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: List[Dict], regiones: List[int]):
        super().__init__(nombre, preguntas)
        self.__regiones = regiones

    def getRegiones(self) -> List[int]:
        return self.__regiones

    def setRegiones(self, regiones: List[int]) -> None:
        self.__regiones = regiones

    def agregarListadoRespuestas(self, listado: ListadoRespuestas) -> None:
        region_usuario = listado.getUsuario().getRegion()
        if region_usuario in self.__regiones:
            super().agregarListadoRespuestas(listado)
        else:
            print("El usuario no pertenece a las regiones permitidas.")
