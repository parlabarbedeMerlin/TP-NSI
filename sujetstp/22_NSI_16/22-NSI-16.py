def maxi(tab):
    val_max = tab[0]
    pos_max = 0
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            pos_max = i
    return (val_max, pos_max)



def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = [] # <- NB : cette ligne est inutile
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

