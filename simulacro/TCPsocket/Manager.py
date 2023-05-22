class Manager:
    respuestas = []
    palabras_fichero = []

    def leer_fichero(self, fichero):
        self.palabras_fichero = []
        with open(fichero) as fs_fichero:
            for linea in fs_fichero:
                self.palabras_fichero.append(linea.strip())
            # return str(self.palabras_fichero)
        return str(self.devolver_respuesta(self.palabras_fichero))

    def devolver_respuesta(self, palabras):
        self.respuestas = []
        for palabra in palabras:
            self.analizar_palindromo(palabra)    
        return self.respuestas
    
    def analizar_palindromo(self, palabra):
        palabraInvertida = palabra[::-1] #iterable[inicio:fin:paso]
        if palabra == palabraInvertida:
            self.respuestas.append(True)
        else: 
            self.respuestas.append(False)