def xor(tab1, tab2):
    assert len(tab1) == len(tab2), "les deux tableaux ne font pas la meme taille"
    resultat = []
    taille = len(tab1)
    for compteur in range(taille):
        resultat.append(tab1[compteur]^tab2[compteur])
    return resultat

class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0)
    for i in range(1, n):
        if carre.somme_ligne(i) != s:
            return False
    for j in range(n):
        if carre.somme_ligne(j) != s:
            return False
    if sum([carre.valeurs[k][k] for k in range(n)]) != s:
        return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
        return False
    return s

c1 = Carre([[1, 1],
            [1, 1]])

c2 = Carre([[2, 9, 4],
            [7, 5, 3],
            [6, 1, 8]])

c3 = Carre([[4, 5, 16, 9],
            [14, 7, 2, 11],
            [3, 10, 15, 6],
            [13, 12, 8, 1]])
