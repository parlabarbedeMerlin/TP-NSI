def nb_repetition(nb,l):
    r = 0
    for i in l :
        r= r+1 if i==nb else r
    return r

print(nb_repetition(12,[1, '! ',7,21,36,44]))

def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a
