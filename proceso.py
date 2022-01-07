import multiplo as mp


def data(long):
    lo = float(long)
    bar = mp.multi(lo)
    return f'se necesita {bar:.0f} barras de hierro'