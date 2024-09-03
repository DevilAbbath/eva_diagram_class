class Alternativa:
    def __init__(self, contenido: str, ayuda: str):
        self.__contenido = contenido
        self.__ayuda = ayuda

    def getContenido(self) -> str:
        return self.__contenido

    def setContenido(self, contenido: str) -> None:
        self.__contenido = contenido

    def getAyuda(self) -> str:
        return self.__ayuda

    def setAyuda(self, ayuda: str) -> None:
        self.__ayuda = ayuda

    def mostrar(self) -> None:
        print(f"Contenido: {self.__contenido}")
        print(f"Ayuda: {self.__ayuda}")
