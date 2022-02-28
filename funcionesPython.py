def sumatoria(arreglo):
    total = 0
    for i in arreglo:
        total += i
    return total

def numeroMayor(arreglo):
    numMayor = arreglo[0]
    for i in arreglo:
        if numMayor < i:
            numMayor = i
    return numMayor

def existeNumero(arreglo, elemento):
    for i in arreglo:
        if(i == elemento):
            return True

    return False

nm = numeroMayor([1, 2, 4, 7, 1])

en = existeNumero([3, 4, 1, 2], 8)
print(en)