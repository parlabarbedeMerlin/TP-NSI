def maxi(tab:list):
    max = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > max:
            max = tab[i]
    return max,tab.index(max)

print(maxi([1,5,6,9,1,2,3,7,9,8]))

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False:
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j = j + 1
        if j == g:
            trouve = True
        i = i + 1
    return trouve

print(recherche("AATC", "GTACAAATCTTGCC"))

print(recherche("AGTC", "GTACAAATCTTGCC"))