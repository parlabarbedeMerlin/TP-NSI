def recherche(elt, tab):
    v=0
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1
print(recherche(1, [10, 12, 1, 56]))

def insere(a, tab):
    r=[]
    insert=True
    for i in tab:
        if a<=i and insert:
            insert=False
            r.append(a)
            r.append(i)
        else:
            r.append(i)
    return r


print(insere(3,[1,2,4,5]))

