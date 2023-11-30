def fib(n) :
  if n < 2 :
    return n
  else :
    return fib(n-1)+fib(n-2)
  
def fib_mem(n):
  mem = [0]*(n+1)  #permet de créer un tableau contenant n+1 zéro
  return fib_mem_c(n,mem)

def fib_mem_c(n,m):
  if n==0 or n==1:
    m[n]=n
    return n
  elif m[n]>0:
    return m[n]
  else:
    m[n]=fib_mem_c(n-1,m) + fib_mem_c(n-2,m)
    return m[n]
  
def algo_glouton(m , S=[500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]):
  i = 0
  T=[]
  while m != 0 :
    if m >= S[i] :
      T.append(S[i])
      m = round(m - S[i],2)
    else :
      i += 1
  return T

def rendu_monnaie_rec(P,X):
  if X==0:
    return 0
  else:
    mini = 1000
  for i in range(len(P)):
    if P[i]<=X:
      nb = 1 + rendu_monnaie_rec(P,X-P[i])
      if nb<mini:
        mini = nb
  return mini

pieces = (2,5,10,50,100)

def rendu_monnaie_mem(P,X):
  mem = [0]*(X+1)
  return rendu_monnaie_mem_c(P,X,mem)

def rendu_monnaie_mem_c(P,X,m):
  if X==0:
    return 0
  elif m[X]>0:
    return m[X]
  else:
    mini = 1000
    for i in range(len(P)):
      if P[i]<=X:
        nb=1+rendu_monnaie_mem_c(P,X-P[i],m)
        if nb<mini:
          mini = nb
          m[X] = mini
  return mini

pieces = (2,5,10,50,100) 