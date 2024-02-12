def hanoi(n, D, A, I):
    if n != 0:
        hanoi(n-1, D, I, A)
        print("deplacer le disque ", D, "vers","A")
        hanoi(n-1, I, A, D)