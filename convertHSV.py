def RGB_HSV(R, G, B):
    RR, GG, BB = R / 255, G / 255, B / 255
    Cmax = max(RR, GG, BB)
    Cmin = min(RR, GG, BB)
    Delta = Cmax - Cmin

    if Cmax == RR:
        try:
            H = ((GG - BB) / (Cmax - Cmin)) * 60
        except ZeroDivisionError:
            H = 0  # O pixel é totalmente vermelho (R255, G000, B000).
    elif Cmax == GG:
        try:
            H = (2.0 + (BB - RR) / (Cmax - Cmin)) * 60
        except ZeroDivisionError:
            H = 120  # O pixel é totalmente verde (R000, G255, B000).
    elif Cmax == BB:
        try:
            H = (4 + (RR - GG) / (Cmax - Cmin)) * 60
        except ZeroDivisionError:
            H = 240  # O pixel é totalmente azul (R000, G000, B255).
    else:
        print('Erro!')

    if H < 0:
        H += 360

    H = f'{H:.0f}'
    try:
        S = f'{(Delta / Cmax) * 100:.1f}'
    except ZeroDivisionError:
        S = 0
    V = f'{Cmax * 100:.1f}'

    HSV_f = (float(H), float(S), float(V))
    HSV_r = (round(HSV_f[0]), round(HSV_f[1]), round(HSV_f[2]))
    HSV = HSV_r

    return HSV
