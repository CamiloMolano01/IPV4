def print_hi(name):
    while True:
        ip = input('Ingrese la IP: ')
        # ip_bin = input('Ingrese la IP en Binario: ')

        ip = bina(ip)
        mask = int(input('Ingrese el prefijo: '))
        mask = llenado(mask)

        print('ip: ')
        print(dev(ip))
        print('mascara: ')
        print(dev(mask))
        print('wildcard/mascara inversa: ')
        print(dev(wildcard(mask)))
        print('direccion de red: ')
        print(dev(de_red_and(ip, mask)))
        print('direccion broadcast: ')
        print(dev(broadcast_or(ip, wildcard(mask))))


def dev(lista):
    ip = ""
    for i in range(0, 32, 8):
        value = 0
        value += (lista[i + 0] * (2 ** 7))
        value += (lista[i + 1] * (2 ** 6))
        value += (lista[i + 2] * (2 ** 5))
        value += (lista[i + 3] * (2 ** 4))
        value += (lista[i + 4] * (2 ** 3))
        value += (lista[i + 5] * (2 ** 2))
        value += (lista[i + 6] * (2 ** 1))
        value += (lista[i + 7] * (2 ** 0))
        ip += str(value) + " "

    return ip


def de_red_and(ip, mask):
    list = []
    for i in range(32):
        if ip[i] == mask[i]:
            list.append(ip[i])
        else:
            list.append(0)

    return list


def broadcast_or(ip, mask_inv):
    list = []
    for i in range(32):
        if ip[i] == 1 or mask_inv[i] == 1:
            list.append(1)
        else:
            list.append(0)

    return list


def bina(ip):
    list = []
    sep = ip.split('.')

    for octecto in sep:
        octecto = int(octecto)
        binario = ''
        while octecto > 0:
            residuo = int(octecto % 2)
            octecto = int(octecto / 2)
            binario = str(residuo) + str(binario)

        while len(binario) < 8:
            binario = '0' + binario

        for b in binario:
            list.append(int(b))

    return list


def llenado(prefijo):
    list = []
    for i in range(prefijo):
        list.append(1)

    for i in range(prefijo, 32):
        list.append(0)

    return list


def wildcard(mask):
    w_mask = mask.copy()
    for i in range(32):
        if w_mask[i] == 1:
            w_mask[i] = 0
        else:
            w_mask[i] = 1
    return w_mask


if __name__ == '__main__':
    print_hi('PyCharm')
