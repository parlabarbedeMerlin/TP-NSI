def conv_bin(n)-> tuple:
    """
    renvoie un couple (b,bit)
    b est une liste d'entiers correspondant à la représentation binaire de n;
    bit correspond aux nombre de bits qui constituent b.
    """
    b = []
    bit = 0
    if n == 0:
        b = [0]
        bit = 1
    while n > 0:
        b.append(n % 2)
        n = n // 2
        bit += 1
    b.reverse()
    return (b, bit)

print(conv_bin(10))

def tri_bulles(T):
    n = len(T)
    for i in range(n-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T