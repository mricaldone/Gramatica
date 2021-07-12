from SeparadorDeSilabas import SeparadorDeSilabas
from SeparadorDeSilabas import NoHayVocal

def separarEnSilabas(texto, separador="-"):
    sepsil = SeparadorDeSilabas()
    return sepsil.separar(texto, separador)