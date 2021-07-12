class SeparadorDeSilabas:

    def __init__(self):
        self.vocales_con_dieresis = ('ü',)
        self.vocales_cerradas_sin_tilde = ('i', 'u')
        self.vocales_cerradas_con_tilde = ('í', 'ú')
        self.vocales_cerradas = self.vocales_cerradas_con_tilde + self.vocales_cerradas_sin_tilde
        self.vocales_abiertas_sin_tilde = ('a', 'e', 'o')
        self.vocales_abiertas_con_tilde = ('á', 'é', 'ó')
        self.vocales_abiertas = self.vocales_abiertas_con_tilde + self.vocales_abiertas_sin_tilde
        self.vocales = self.vocales_abiertas + self.vocales_cerradas + self.vocales_con_dieresis
        self.grupos_consonanticos = ('br', 'cr', 'dr', 'gr', 'fr', 'kr', 'tr', 'bl', 'cl', 'gl', 'fl', 'kl', 'pl', 'pr', 'ch', 'rr', 'll')
        self.separadores = (' ', '\n', '\t')

    def separar(self, texto):
        resultado = ""
        palabra = ""
        for letra in texto:
            palabra += letra
            if self._es_separador(letra):
                resultado += self._separar_palabra(palabra)
                palabra = ""
        resultado += self._separar_palabra(palabra)
        return resultado

    def _es_separador(self, caracter):
        return caracter in self.separadores

    def _es_vocal(self, letra):
        return letra.lower() in self.vocales

    def _es_vocal_abierta(self, letra):
        return letra.lower() in self.vocales_abiertas

    def _es_vocal_cerrada(self, letra):
        return letra.lower() in self.vocales_cerradas

    def _es_vocal_abierta_sin_tilde(self, letra):
        return letra.lower() in self.vocales_abiertas_sin_tilde

    def _es_vocal_abierta_con_tilde(self, letra):
        return letra.lower() in self.vocales_abiertas_con_tilde

    def _es_vocal_cerrada_sin_tilde(self, letra):
        return letra.lower() in self.vocales_cerradas_sin_tilde

    def _es_vocal_cerrada_con_tilde(self, letra):
        return letra.lower() in self.vocales_cerradas_con_tilde

    def _es_hiato(self, letra_a, letra_b):
        if self._es_vocal_abierta_sin_tilde(letra_a) and self._es_vocal_cerrada_con_tilde(letra_b):
            return True
        if self._es_vocal_cerrada_con_tilde(letra_a) and self._es_vocal_abierta_sin_tilde(letra_b):
            return True
        if self._es_vocal_abierta(letra_a) and self._es_vocal_abierta(letra_b):
            return True
        if letra_a == letra_b and self._es_vocal(letra_a):
            return True
        return False

    def _es_grupo_consonantico(self, par):
        return par.lower() in self.grupos_consonanticos

    def _buscar_vocal(self, palabra):
        for index,letra in enumerate(palabra):
            if self._es_vocal(letra):
                return index
        raise NoHayVocal

    def _separar_palabra(self, palabra):
        try:
            primera_vocal = self._buscar_vocal(palabra)
            segunda_vocal = primera_vocal + self._buscar_vocal(palabra[primera_vocal + 1:len(palabra)]) + 1
            if segunda_vocal - primera_vocal - 1 == 0:
                if not self._es_hiato(palabra[primera_vocal], palabra[segunda_vocal]):
                    segunda_vocal = segunda_vocal + self._buscar_vocal(palabra[segunda_vocal + 1:len(palabra)]) + 1
            if segunda_vocal - primera_vocal - 1 == 2:
                if not self._es_grupo_consonantico(palabra[primera_vocal + 1:primera_vocal + 3]):
                    return palabra[:segunda_vocal - 1] + "-" + self._separar_palabra(palabra[segunda_vocal - 1:len(palabra)])
            if segunda_vocal - primera_vocal - 1 == 3:
                if self._es_grupo_consonantico(palabra[primera_vocal + 2:primera_vocal + 4]):
                    return palabra[:primera_vocal + 2] + "-" + self._separar_palabra(palabra[primera_vocal + 2:len(palabra)])
                else:
                    return palabra[:primera_vocal + 3] + "-" + self._separar_palabra(palabra[primera_vocal + 3:len(palabra)])
            if segunda_vocal - primera_vocal - 1 == 4:
                return palabra[:segunda_vocal - 2] + "-" + self._separar_palabra(palabra[segunda_vocal - 2:len(palabra)])
            return palabra[:primera_vocal + 1] + "-" + self._separar_palabra(palabra[primera_vocal + 1:len(palabra)])
        except NoHayVocal:
            return palabra

class NoHayVocal(Exception):
    pass