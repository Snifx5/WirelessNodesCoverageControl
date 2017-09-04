#import numpy as np

#Función de cobertura
#def f(x):
#    return x**3

# Rango del sector a cubrir en x y Y
L = 5
# Radio de cobertura de cada nodo
R = 1
# Cantidad de nodos
P = 3
xlist = [i for i in range(P)]
ylist = [i for i in range(P)]
# pairs vector conteniente la posición de cada nodo
pairs = [[x, y] for x, y in zip(xlist, ylist)]

maps = [[[0 for k in range(L)] for j in range(L)] for i in range(P)]
#maps [0][0][0]= ((i-xlist(P))**2+(j-ylist(P))**2)<=R**2
#Función de cobertura para cada nodo
activiti_vector = [ 0, 0 , 1]
v_a = [ activiti_vector[k]== 1 for k in range(P)]
for k in range(P):
    if v_a[k] == 1:
        maps[k]=  [[ ((i-xlist[k])**2+(j-ylist[k])**2)<=R**2 for j in range(L)] for i in range(L)]
    else:
        maps[k] = [[ i+j==-1 for j in range(L)] for i in range(L)]
#Cobertura total del sistema de P nodos activos

T = maps[0]
for k in range(P):
   T = [[T[j][i]|maps[k][j][i] for j in range(L)] for i in range(L)]

suma = [sum(T[k]) for k in range (L)]
suma = sum(suma)
#Matriz total de cobertura
print (T, pairs, suma)