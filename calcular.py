from math import ceil


def datos(longitud, traslape, diametro):
    longitud = float(longitud)

    if traslape == 0:
        barra = __multiplo(longitud)
        dist = barra*12.0
        return f'Se necesita {barra:.0f} barras de hierro, con una longitud de {dist:.2f}.m'

    if traslape == 1:
        barra = __multiplo(longitud)
        dist = (barra*12)+((barra-1)*diametro)
        return f'Se necesita {barra:.0f} barras de hierro, con una longitud de {dist:.2f}m.'


def __multiplo(barra):
    # print(barra, type(barra))
    if barra % 12 == 0:
        division = barra/12
        return division
    else:
        division = barra/12
        redondeado = ceil(division)
        return redondeado
