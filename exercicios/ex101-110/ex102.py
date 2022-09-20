def fatorial(n, show=False):
    """
    -> Calculate the factorial of a number
    :param n: The number to be calculated.
    :param show: (optional) show or not the calculation.
    :return: The factorial value of a number n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# PROGRAMA PRINCIPAL
print(fatorial(5, show=True))
help(fatorial)
