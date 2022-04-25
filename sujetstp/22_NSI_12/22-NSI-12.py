def moyenne(tab=[]):
    if(tab==[]):
        print('erreur')
        return None
    else:
        somme=0
        for i in tab:
            somme+=i
        return somme/len(tab)

print(moyenne([]))


def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i+=1
        else :
            tab[i],tab[j] = tab[j],tab[i]
            j-=1
    return tab

print(tri([0,1,0,1,0,1,0,1,0]))