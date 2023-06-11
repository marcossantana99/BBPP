#Buenas Practicas de Programación en Python
#Practica 4 realizada por Marcos Santana Pastor


#1 Parte
#import pdb 
#pdb.set_trace()

def max_list (L): 
    M = [max(L[i]) for i in range(0,len(L))]
    return M

L = [[2,4,1],[1,2,3,4,5,6,7,8],[100,250,43]]
print(max_list(L))

#2 Parte

def comprobar (x):
    
    if x == 2:
        return True
    else:

        m = [i for i in range(2,x)]
        j = 0
        while (j <= (len(m)-1)) and (x%m[j] != 0):
            j = j+1
        
        return j == len(m)
 

def filt_primos (L): 
    P = list(filter(comprobar, L))
    return P

L = [3, 4, 8, 5, 5, 22, 13]
print(filt_primos (L))