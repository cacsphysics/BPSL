# Created by Beloit Plasma Science Group

me = 9.109e-31  # Electron mass in kg
mp = 1.673e-27  # proton mass in kg


def ion_cyclotron(B, m=mp, q=1.602e-19):
    """
    Outputs the ion cyclotron frequency:
    Inputs:
        m - mass (kg)
        B - magnetic field (T)
        q - charge (C)

    Outputs:
        wc - cyclotron frequency (rad/s)
    """
    wc = q * B / m

    return wc


def e_cyclotron(B):
    """
    Outputs the electron cyclotron frequency:
    Inputs:
        B - magnetic field (T)

    Outputs:
        wce - electron frequency (rad/s)
    """
    wce = (1.602e-19) * B / me

    return wce
