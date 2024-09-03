from typing import List
from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, ayuda: str, requerida: bool, alternativas: List[Alternativa]):
        self.__enunciado = enunciado
        self.__ayuda = ayuda
        self.__requerida = requerida
        self.__alternativas = alternativas

    def getEnunciado(self) -> str:
        return self.__enunciado

    def setEnunciado(self, enunciado: str) -> None:
        self.__enunciado = enunciado

    def getAyuda(self) -> str:
        return self.__ayuda

    def setAyuda(self, ayuda: str) -> None:
        self.__ayuda = ayuda

    def isRequerida(self) -> bool:
        return self.__requerida

    def setRequerida(self, requerida: bool) -> None:
        self.__requerida = requerida

    def getAlternativas(self) -> List[Alternativa]:
        return self.__alternativas

    def mostrar(self) -> None:
        print(f"Enunciado: {self.__enunciado}")
        print(f"Ayuda: {self.__ayuda}")
        print(f"Requerida: {'Sí' if self.__requerida else 'No'}")
        print("Alternativas:")
        for alternativa in self.__alternativas:
            alternativa.mostrar()
