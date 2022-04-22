def recherche(L):
    r = []
    for i in range(1, len(L)):
        if L[i] == (L[i - 1] + 1):
            r.append((L[i - 1], L[i]))
    return r


print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]


def propager(M, i, j, val):
    if M[i][j] == val:
        return
    d=M[i][j]
    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if (i - 1) >= 0 and M[i - 1][j] == d:
        propager(M, i - 1, j, val)

    # l'élément en bas fait partie de la composante
    if (i + 1) < len(M) and M[i + 1][j] == d:
        propager(M, i + 1, j, val)

    # l'élément à gauche fait partie de la composante
    if (j - 1) >= 0 and M[i][j - 1] == d:
        propager(M, i, j - 1, val)

    # l'élément à droite fait partie de la composante
    if (j + 1) < len(M[0]) and M[i][j + 1] == d:
        propager(M, i, j + 1, val)


for i in M:
    print(i)

propager(M, 2, 1, 3)


print("\n\n\n\n")
for j in M:
    print(j)
