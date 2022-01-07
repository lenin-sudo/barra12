from math import ceil


def datos(longitud):

    longitud = float(longitud)
    barra = __multiplo(longitud)
    # print(barra, type(barra))
    return f'Se necesita {barra:.0f} barras de hierro'


def __multiplo(barra):
    # print(barra, type(barra))
    if barra % 12 == 0:
        division = barra/12

        return division
    else:
        division = barra/12
        redondeado = ceil(division)
        return redondeado
