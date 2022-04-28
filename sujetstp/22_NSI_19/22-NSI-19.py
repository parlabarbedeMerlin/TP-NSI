def multiplication(a,b):
    r=0
    for i in range(a):
        r+=b
    return r

print(multiplication(3,2))


def chercher(T, n, i, j):
    if i < 0 or j >= len(T) :
        print('Erreur')
        return None
    if i > j :
        return None
    m = (i + j) // 2
    if T[m] < n :
        return chercher(T, n, m + 1, j)
    elif T[m] > n :
        return chercher(T, n, i, m - 1 )
    else :
        return m