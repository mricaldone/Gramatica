import Gramatica

def testSeparadorDeSilabas(entrada, esperado):
    try:
        salida = Gramatica.separarEnSilabas(entrada)
    except Gramatica.NoHayVocal:
        print("[ERROR]","Salida esperada:", "\"" + esperado + "\"", "|", "Salida obtenida:", "Excepcion: No hay vocal")
        return
    if esperado != salida:
        print("[ERROR]","Salida esperada:", "\"" + esperado + "\"", "|", "Salida obtenida:", "\"" + salida + "\"")
    else:
        print("[OK]","Entrada:", "\"" + entrada + "\"", "|", "Salida:", "\"" + salida + "\"")

testSeparadorDeSilabas("AprEnDer", "A-prEn-Der")
testSeparadorDeSilabas("ÉpiCo", "É-pi-Co")
testSeparadorDeSilabas("PÓDIO", "PÓ-DIO")
testSeparadorDeSilabas("aprender", "a-pren-der")
testSeparadorDeSilabas("tabla", "ta-bla")
testSeparadorDeSilabas("ratón", "ra-tón")
testSeparadorDeSilabas("épico", "é-pi-co")
testSeparadorDeSilabas("brocha", "bro-cha") # grupos consonanticos br, cr, dr, gr, fr, kr, tr, bl, cl, gl, fl, kl, pl son inseparables
testSeparadorDeSilabas("abrazo", "a-bra-zo")
testSeparadorDeSilabas("submarino", "sub-ma-ri-no") # los prefijos pueden o no separarse
testSeparadorDeSilabas("perspicacia", "pers-pi-ca-cia") # 3 consonantes consecutivas, 2 van a la silaba anterior y 1 a la siguiente
testSeparadorDeSilabas("conspirar", "cons-pi-rar")
testSeparadorDeSilabas("obscuro", "obs-cu-ro")
testSeparadorDeSilabas("irreal", "i-rre-al") # no se pueden separar las rr
testSeparadorDeSilabas("acallar", "a-ca-llar") # no se pueden separar las ll
testSeparadorDeSilabas("abstracto", "abs-trac-to") # 4 consonantes consecutivas, 2 van a la silaba anterior y 2 a la siguiente
testSeparadorDeSilabas("rubia", "ru-bia") # los diptongos no se separan
testSeparadorDeSilabas("labio", "la-bio")
testSeparadorDeSilabas("caigo", "cai-go")
testSeparadorDeSilabas("oigo", "oi-go")
testSeparadorDeSilabas("descafeinado", "des-ca-fei-na-do")
testSeparadorDeSilabas("diurno", "diur-no")
testSeparadorDeSilabas("ruido", "rui-do")
testSeparadorDeSilabas("pódio", "pó-dio")
testSeparadorDeSilabas("aplanar", "a-pla-nar")
testSeparadorDeSilabas("ocre", "o-cre")
testSeparadorDeSilabas("archi", "ar-chi")
testSeparadorDeSilabas("leer", "le-er")
testSeparadorDeSilabas("caos", "ca-os")
testSeparadorDeSilabas("baúl", "ba-úl")
testSeparadorDeSilabas("ambiguo", "am-bi-guo")
testSeparadorDeSilabas("antifaz", "an-ti-faz")
testSeparadorDeSilabas("transplantar", "trans-plan-tar")
testSeparadorDeSilabas("substraer", "subs-tra-er")
testSeparadorDeSilabas("abstraer", "abs-tra-er")
testSeparadorDeSilabas("abstracto", "abs-trac-to")
testSeparadorDeSilabas("pingüino", "pin-güi-no")
testSeparadorDeSilabas("vergüenza", "ver-güen-za")
testSeparadorDeSilabas("bilingüe", "bi-lin-güe")
testSeparadorDeSilabas("baúl ocre", "ba-úl o-cre")
testSeparadorDeSilabas("", "")
testSeparadorDeSilabas(" ", " ")
testSeparadorDeSilabas("  ", "  ")
testSeparadorDeSilabas("k", "k")
testSeparadorDeSilabas("1", "1")
testSeparadorDeSilabas("abstraer  abstracto", "abs-tra-er  abs-trac-to")