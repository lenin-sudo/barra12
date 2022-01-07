from math import ceil


def multi(valor):
    if valor % 12 == 0:
        div = valor/12
        return div
    else:
        div = valor/12
        cei = ceil(div)
        return cei