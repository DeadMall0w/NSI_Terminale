tab = [[5], 
    [8, 10 ], 
    [11, 3, 4], 
    [6, 10, 7, 12 ]]


def G(l,c):
    if l >= len(tab)-1:
        return tab[l][c]
    return max(G(l+1,c), G(l+1,c+1))+tab[l][c]

def G_mem():
    m = []
    for x in range(len(tab)):
        t = []
        for y in range(len(tab[x])):
            t.append(0)
        m.append(t)
    return G_mem_c(0,0,m)

def G_mem_c(l,c,m):
    if l >= len(tab)-1:
        return tab[l][c]
    elif m[l][c] != 0:
        return m[l][c]
    v =  max(G_mem_c(l+1,c,m), G_mem_c(l+1,c+1,m))+tab[l][c]
    m[l][c] = v
    return v

print(G_mem())
# print(tab)