import random
import math
import pickle #ce module nous permettra d'enregistrer la liste de tous les tétraèdre de Sierpinski construits

T=[] #on crée une liste vide dans laquelle nous enregistrerons plus tard les tétraèdres de Sierpinski complets que nous trouverons

#Hello Clara

#on déclare d'abord les variables libres de notre système en tant qu'entiers choisis aléatoirement entre 1 et 500
a1 = int(random.randint(1,500))
print("a1=",a1)

b1 = int(random.randint(1,500))
print("b1=",b1)

d1 = int(random.randint(1,500))
print("d1=",d1)

g1 = int(random.randint(1,500))
print("g1=",g1)

h1 = int(random.randint(1,500))
print("h1=",h1)

a2 = int(random.randint(1,500))
print("a2=",a2)

b2 = int(random.randint(1,500))
print("b2=",b2)

d2 = int(random.randint(1,500))
print("d2=",d2)

e2 = int(random.randint(1,500))
print("e2=",e2)

g2 = int(random.randint(1,500))
print("g2=",g2)

a3 = int(random.randint(1,500))
print("a3=",a3)

b3 = int(random.randint(1,500))
print("b3=",b3)

d3 = int(random.randint(1,500))
print("d3=",d3)

g3 = int(random.randint(1,500))
print("g3=",g3)

b4 = int(random.randint(1,500))
print("b4=",b4)

d4 = int(random.randint(1,500))
print("d4=",d4)

g4 = int(random.randint(1,500))
print("g4=",g4)

#on déclare ensuite la somme magique M du tétraèdre comme un entier aléatoirement compris entre 500 et 1500
#ce choix nous permet en effet de nous assurer que la somme magique sera au moins plus grande que les variables libres du tétraèdre, et ainsi augmenter nos chances d'avoir dès le départ une valeur de M strictement plus grande que les entiers présents dans le tétraèdre
M = int(random.randint(500,1500))
print("M=",M)

#on définit une fonction prenant comme arguments les variables libres et la somme magique précédemment définies
def tetrahedron_sierpinski(a1,b1,d1,g1,h1,a2,b2,d2,e2,g2,a3,b3,d3,g3,b4,d4,g4,M):
    
    #on déclare les variables liées de notre système, qu'on définit en tant qu'entiers
    c1 = int()
    e1 = int()
    f1 = int()
    i1 = int()
    j1 = int()
    k1 = int()
    l1 = int()
    c2 = int()
    f2 = int()
    h2 = int()
    i2 = int()
    j2 = int()
    k2 = int()
    l2 = int()
    c3 = int()
    e3 = int()
    f3 = int()
    h3 = int()
    i3 = int()
    j3 = int()
    k3 = int()
    l3 = int()
    a4 = int()
    c4 = int()
    e4 = int()
    f4 = int()
    h4 = int()
    i4 = int()
    j4 = int()
    k4 = int()
    l4 = int()
    
    #on commence par vérifier que toutes les variables libres sont distinctes deux à deux
    if a1!=b1 and a1!=d1 and a1!=g1 and a1!=h1 and a1!=a2 and a1!=b2 and a1!=d2 and a1!=e2 and a1!=g2 and a1!=a3 and a1!=b3 and a1!=d3 and a1!=g3 and a1!=d4 and a1!=g4 and b1!=d1 and b1!=g1 and b1!=h1 and b1!=a2 and b1!=b2 and b1!=d2 and b1!=e2 and b1!=g2 and b1!=a3 and b1!=b3 and b1!=d3 and b1!=g3 and b1!=d4 and b1!=g4 and d1!=g1 and d1!=h1 and d1!=a2 and d1!=b2 and d1!=d2 and d1!=e2 and d1!=g2 and d1!=a3 and d1!=b3 and d1!=d3 and d1!=g3 and d1!=d4 and d1!=g4 and g1!=h1 and g1!=a2 and g1!=b2 and g1!=d2 and g1!=e2 and g1!=g2 and g1!=a3 and g1!=b3 and g1!=d3 and g1!=g3 and g1!=d4 and d1!=g4 and h1!=a2 and h1!=b2 and h1!=d2 and h1!=e2 and h1!=g2 and h1!=a3 and h1!=b3 and h1!=d3 and h1!=g3 and h1!=g3 and h1!=d4 and h1!=g4 and a2!=b2 and a2!=d2 and a2!=e2 and a2!=g2 and a2!=a3 and a2!=b3 and a2!=d3 and a2!=g3 and a2!=d4 and a2!=g4 and b2!=d2 and b2!=e2 and b2!=g2 and b2!=g2 and b2!=a3 and b2!=b3 and b2!=d3 and b2!=g3 and b2!=d4 and b2!=g4 and d2!=e2 and d2!=g2 and d2!=a3 and d2!=b3 and d2!=d3 and d2!=g3 and d2!=d4 and d2!=g4 and e2!=g2 and e2!=a3 and e2!=b3 and e2!=d3 and e2!=g3 and e2!=d4 and e2!=g4 and g2!=a3 and g2!=b3 and g2!=d3 and g2!=g3 and g2!=d4 and g2!=g4 and a3!=b3 and a3!=d3 and a3!=g3 and a3!=d4 and a3!=g4 and b3!=d3 and b3!=g3 and b3!=d4 and b3!=g4 and d3!=g3 and d3!=d4 and d3!=g4 and g3!=d4 and g3!=g4 and d4!=g4 and b4!=d4 and b4!=g4 and b4!=a1 and b4!=b1 and b4!=d1 and b4!=h1 and b4!=a2 and b4!=b2 and b4!=e2 and b4!=g2 and b4!=a3 and b4!=b3 and b4!=d3 and b4!=g3:
        #si c'est bien le cas, on continue en vérifiant que la valeur de M est strictement supérieure à celle de la somme de a1 et b1
        if M>(a1+b1):
            c1 = M-(a1+b1) #on assigne à c1 la valeur de M-(a1+b1) si on a bien M>(a1+b1)
            print("c1=",c1)
            #on réitère ce processus avec les différents entiers du tétraèdre que l'on cherche à construire
            if M>(g1+h1):
                i1 = M-(g1+h1)
                print("i1=",i1)
                if M>(b1+g1):
                    j1 = M-(b1+g1)
                    print("j1=",j1)
                    if M>(c1+d1):
                        k1 = M-(c1+d1)
                        print("k1=",k1)
                        if M>(j1+k1):
                            l1 = M-(j1+k1)
                            print("l1=",l1)
                            if M>(i1+l1):
                                e1 = M-(i1+l1)
                                print("e1=",e1)
                                if M>(d1+e1):
                                    f1 = M-(d1+e1)
                                    print("f1=",f1)
                                    if M>(a2+b2):
                                        c2 = M-(a2+b2)
                                        print("c2=",c2)
                                        if M>(d2+e2):
                                            f2 = M-(d2+e2)
                                            print("f2=",f2)
                                            if M>(a2+f2):
                                                h2 = M-(a2+f2)
                                                print("h2=",h2)
                                                if M>(g2+h2):
                                                    i2 = M-(g2+h2)
                                                    print("i2=",i2)
                                                    if M>(b2+g2):
                                                        j2 = M-(b2+g2)
                                                        print("j2=",j2)
                                                        if M>(c2+d2):
                                                            k2 = M-(c2+d2)
                                                            print("k2=",k2)
                                                            if M>(i2+e2):
                                                                l2 = M-(i2+e2)
                                                                print("l2=",l2)
                                                                if M>(a3+b3):
                                                                    c3 = M-(a3+b3)
                                                                    print("c3=",c3)
                                                                    if M>(b3+g3):
                                                                        j3 = M-(b3+g3)
                                                                        print("j3=",j3)
                                                                        if M>(c3+d3):
                                                                            k3 = M-(c3+d3)
                                                                            print("k3=",k3)
                                                                            if M>(j3+k3):
                                                                                l3 = M-(j3+k3)
                                                                                print("l3=",l3)
                                                                                if M>(a1+f2):
                                                                                    h3 = M-(a1+f2)
                                                                                    print("h3=",h3)
                                                                                    if M>(a3+h3):
                                                                                        f3 = M-(a3+h3)
                                                                                        print("f3=",f3)
                                                                                        if M>(d3+f3):
                                                                                            e3 = M-(d3+f3)
                                                                                            print("e3=",e3)
                                                                                            if M>(g3+h3):
                                                                                                i3 = M-(g3+h3)
                                                                                                print("i3=",i3)
                                                                                                if M>(h1+a3):
                                                                                                    f4 = M-(h1+a3)
                                                                                                    print("f4=",f4)
                                                                                                    if M>(d4+f4):
                                                                                                        e4 = M-(d4+f4)
                                                                                                        print("e4=",e4)
                                                                                                        if M>(h2+f3):
                                                                                                            a4 = M-(h2+f3)
                                                                                                            print("a4=",a4)
                                                                                                            if M>(f1+a2):
                                                                                                                h4 = M-(f1+a2)
                                                                                                                print("h4=",h4)
                                                                                                                if M>(g4+h4):
                                                                                                                    i4 = M-(g4+h4)
                                                                                                                    print("i4=",i4)
                                                                                                                    if M>(e4+i4):
                                                                                                                        l4 = M-(e4+i4)
                                                                                                                        print("l4=",l4)
                                                                                                                        if M>(a4+b4):
                                                                                                                            c4 = M-(a4+b4)
                                                                                                                            print("c4=",c4)
                                                                                                                            if M>(b4+g4):
                                                                                                                                j4 = M-(b4+g4)
                                                                                                                                print("j4=",j4)
                                                                                                                                if M>(c4+d4):
                                                                                                                                    k4 = M-(c4+d4)
                                                                                                                                    print("k4=",k4)
                                                                                                                                    #si tous les entiers du tétraèdre ont pu être consrtuits, on vérifie finalement que les variables liées sont toutes distinctes des variables libres
                                                                                                                                    if a1!=c1 and a1!=e1 and a1!=f1 and a1!=i1 and a1!=j1 and a1!=k1 and a1!=l1 and a1!=c2 and a1!=f2 and a1!=h2 and a1!=i2 and a1!=j2 and a1!=k2 and a1!=l2 and a1!=c3 and a1!=e3 and a1!=f3 and a1!=h3 and a1!=i3 and a1!=j3 and a1!=k3 and a1!=l3 and a1!=a4 and a1!=c4 and a1!=e4 and a1!=f4 and a1!=h4 and a1!=i4 and a1!=j4 and a1!=k4 and a1!=l4 and b1!=c1 and b1!=e1 and b1!=f1 and b1!=i1 and b1!=j1 and b1!=k1 and b1!=l1 and b1!=c2 and b1!=f2 and b1!=h2 and b1!=i2 and b1!=j2 and b1!=k2 and b1!=l2 and b1!=c3 and b1!=e3 and b1!=f3 and b1!=h3 and b1!=i3 and b1!=j3 and b1!=k3 and b1!=l3 and b1!=a4 and b1!=c4 and b1!=e4 and b1!=f4 and b1!=h4 and b1!=i4 and b1!=j4 and b1!=k4 and b1!=l4 and d1!=c1 and d1!=e1 and d1!=f1 and d1!=i1 and d1!=j1 and d1!=k1 and d1!=l1 and d1!=c2 and d1!=f2 and d1!=h2 and d1!=i2 and d1!=j2 and d1!=k2 and d1!=l2 and d1!=c3 and d1!=e3 and d1!=f3 and d1!=h3 and d1!=i3 and d1!=j3 and d1!=k3 and d1!=l3 and d1!=a4 and d1!=c4 and d1!=e4 and d1!=f4 and d1!=h4 and d1!=i4 and d1!=j4 and d1!=k4 and d1!=l4 and g1!=c1 and g1!=e1 and g1!=f1 and g1!=i1 and g1!=j1 and g1!=k1 and g1!=l1 and g1!=c2 and g1!=f2 and g1!=h2 and g1!=i2 and g1!=j2 and g1!=k2 and g1!=l2 and g1!=c3 and g1!=e3 and g1!=f3 and g1!=h3 and g1!=i3 and g1!=j3 and g1!=k3 and g1!=l3 and g1!=a4 and g1!=c4 and g1!=e4 and g1!=f4 and g1!=h4 and g1!=i4 and g1!=j4 and g1!=k4 and g1!=l4 and h1!=c1 and h1!=e1 and h1!=f1 and h1!=i1 and h1!=j1 and h1!=k1 and h1!=l1 and h1!=c2 and h1!=f2 and h1!=h2 and h1!=i2 and h1!=j2 and h1!=k2 and h1!=l2 and h1!=c3 and h1!=e3 and h1!=f3 and h1!=h3 and h1!=i3 and h1!=j3 and h1!=k3 and h1!=l3 and h1!=a4 and h1!=c4 and h1!=e4 and h1!=f4 and h1!=h4 and h1!=i4 and h1!=j4 and h1!=k4 and h1!=l4 and a2!=c1 and a2!=e1 and a2!=f1 and a2!=i1 and a2!=j1 and a2!=k1 and a2!=l1 and a2!=c2 and a2!=f2 and a2!=h2 and a2!=i2 and a2!=j2 and a2!=k2 and a2!=l2 and a2!=c3 and a2!=e3 and a2!=f3 and a2!=h3 and a2!=i3 and a2!=j3 and a2!=k3 and a2!=l3 and a2!=a4 and a2!=c4 and a2!=e4 and a2!=f4 and a2!=h4 and a2!=i4 and a2!=j4 and a2!=k4 and a2!=l4 and b2!=c1 and b2!=e1 and b2!=f1 and b2!=i1 and b2!=j1 and b2!=k1 and b2!=l1 and b2!=c2 and b2!=f2 and b2!=h2 and b2!=i2 and b2!=j2 and b2!=k2 and b2!=l2 and b2!=c3 and b2!=e3 and b2!=f3 and b2!=h3 and b2!=i3 and b2!=j3 and b2!=k3 and b2!=l3 and b2!=a4 and b2!=c4 and b2!=e4 and b2!=f4 and b2!=h4 and b2!=i4 and b2!=j4 and b2!=k4 and b2!=l4 and d2!=c1 and d2!=e1 and d2!=f1 and d2!=i1 and d2!=j1 and d2!=k1 and d2!=l1 and d2!=c2 and d2!=f2 and d2!=h2 and d2!=i2 and d2!=j2 and d2!=k2 and d2!=l2 and d2!=c3 and d2!=e3 and d2!=f3 and d2!=h3 and d2!=i3 and d2!=j3 and d2!=k3 and d2!=l3 and d2!=a4 and d2!=c4 and d2!=e4 and d2!=f4 and d2!=h4 and d2!=i4 and d2!=j4 and d2!=k4 and d2!=l4 and e2!=c1 and e2!=e1 and e2!=f1 and e2!=i1 and e2!=j1 and e2!=k1 and e2!=l1 and e2!=c2 and e2!=f2 and e2!=h2 and e2!=i2 and e2!=j2 and e2!=k2 and e2!=l2 and e2!=c3 and e2!=e3 and e2!=f3 and e2!=h3 and e2!=i3 and e2!=j3 and e2!=k3 and e2!=l3 and e2!=a4 and e2!=c4 and e2!=e4 and e2!=f4 and e2!=h4 and e2!=i4 and e2!=j4 and e2!=k4 and e2!=l4 and g2!=c1 and g2!=e1 and g2!=f1 and g2!=i1 and g2!=j1 and g2!=k1 and g2!=l1 and g2!=c2 and g2!=f2 and g2!=h2 and g2!=i2 and g2!=j2 and g2!=k2 and g2!=l2 and g2!=c3 and g2!=e3 and g2!=f3 and g2!=h3 and g2!=i3 and g2!=j3 and g2!=k3 and g2!=l3 and g2!=a4 and g2!=c4 and g2!=e4 and g2!=f4 and g2!=h4 and g2!=i4 and g2!=j4 and g2!=k4 and g2!=l4 and a3!=i1 and a3!=j1 and a3!=k1 and a3!=l1 and a3!=c2 and a3!=f2 and a3!=h2 and a3!=i2 and a3!=j2 and a3!=k2 and a3!=l2 and a3!=c3 and a3!=e3 and a3!=f3 and a3!=h3 and a3!=i3 and a3!=j3 and a3!=k3 and a3!=l3 and a3!=a4 and a3!=c4 and a3!=e4 and a3!=f4 and a3!=h4 and a3!=i4 and a3!=j4 and a3!=k4 and a3!=l4 and b3!=c1 and b3!=e1 and b3!=f1 and b3!=i1 and b3!=j1 and b3!=k1 and b3!=l1 and b3!=c2 and b3!=f2 and b3!=h2 and b3!=i2 and b3!=j2 and b3!=k2 and b3!=l2 and b3!=c3 and b3!=e3 and b3!=f3 and b3!=h3 and b3!=i3 and b3!=j3 and b3!=k3 and b3!=l3 and b3!=a4 and b3!=c4 and b3!=e4 and b3!=f4 and b3!=h4 and b3!=i4 and b3!=j4 and b3!=k4 and b3!=l4 and d3!=c1 and d3!=e1 and d3!=f1 and d3!=i1 and d3!=j1 and d3!=k1 and d3!=l1 and d3!=c2 and d3!=f2 and d3!=h2 and d3!=i2 and d3!=j2 and d3!=k2 and d3!=l2 and d3!=c3 and d3!=e3 and d3!=f3 and d3!=h3 and d3!=i3 and d3!=j3 and d3!=k3 and d3!=l3 and d3!=a4 and d3!=c4 and d3!=e4 and d3!=f4 and d3!=h4 and d3!=i4 and d3!=j4 and d3!=k4 and d3!=l4 and g3!=c1 and g3!=e1 and g3!=f1 and g3!=i1 and g3!=j1 and g3!=k1 and g3!=l1 and g3!=c2 and g3!=f2 and g3!=h2 and g3!=i2 and g3!=j2 and g3!=k2 and g3!=l2 and g3!=c3 and g3!=e3 and g3!=f3 and g3!=h3 and g3!=i3 and g3!=j3 and g3!=k3 and g3!=l3 and g3!=a4 and g3!=c4 and g3!=e4 and g3!=f4 and g3!=h4 and g3!=i4 and g3!=j4 and g3!=k4 and g3!=l4 and b4!=c1 and b4!=e1 and b4!=f1 and b4!=i1 and b4!=j1 and b4!=k1 and b4!=l1 and b4!=c2 and b4!=f2 and b4!=h2 and b4!=i2 and b4!=j2 and b4!=k2 and b4!=l2 and b4!=c3 and b4!=e3 and b4!=f3 and b4!=h3 and b4!=i3 and b4!=j3 and b4!=k3 and b4!=l3 and b4!=a4 and b4!=c4 and b4!=e4 and b4!=f4 and b4!=h4 and b4!=i4 and b4!=j4 and b4!=k4 and b4!=l4 and d4!=c1 and d4!=e1 and d4!=f1 and d4!=i1 and d4!=j1 and d4!=k1 and d4!=l1 and d4!=c2 and d4!=f2 and d4!=h2 and d4!=i2 and d4!=j2 and d4!=k2 and d4!=l2 and d4!=c3 and d4!=e3 and d4!=f3 and d4!=h3 and d4!=i3 and d4!=j3 and d4!=k3 and d4!=l3 and d4!=a4 and d4!=c4 and d4!=e4 and d4!=f4 and d4!=h4 and d4!=i4 and d4!=j4 and d4!=k4 and d4!=l4 and g4!=c1 and g4!=e1 and g4!=f1 and g4!=i1 and g4!=j1 and g4!=k1 and g4!=l1 and g4!=c2 and g4!=f2 and g4!=h2 and g4!=i2 and g4!=j2 and g4!=k2 and g4!=l2 and g4!=c3 and g4!=e3 and g4!=f3 and g4!=h3 and g4!=i3 and g4!=j3 and g4!=k3 and g4!=l3 and g4!=a4 and g4!=c4 and g4!=e4 and g4!=f4 and g4!=h4 and g4!=i4 and g4!=j4 and g4!=k4 and g4!=l4:
                                                                                                                                    #si tous les entiers sont bien distincts deux à deux, on imprime le tétraèdre de Sierpinski correspondant
                                                                                                                                        row1 = [a1]
                                                                                                                                        row2 = [b1,c1]
                                                                                                                                        row3 = [g1,j1,k1,d1]
                                                                                                                                        row4 = [h1,i1,l1,e1,f1]
                                                                                                                                        row5 = [a3,f4,e4,l4,i4,h4,a2]
                                                                                                                                        row6 = [b3,c3,d4,k4,j4,g4,b2,c2]
                                                                                                                                        row7 = [g3,j3,k3,d3,c4,b4,g2,j2,k2,d2]
                                                                                                                                        row8 = [h3,i3,l3,e3,f3,a4,h2,i2,l2,e2,f2]

                                                                                                                                        print(row1)
                                                                                                                                        print(row2)
                                                                                                                                        print(row3)
                                                                                                                                        print(row4)
                                                                                                                                        print(row5)
                                                                                                                                        print(row6)
                                                                                                                                        print(row7)
                                                                                                                                        print(row8)
                                                                                                                                        
                                                                                                                                        #on ajoute finalement les lignes de notre tétraèdre à la liste T
                                                                                                                                        T.append(row1)
                                                                                                                                        T.append(row2)
                                                                                                                                        T.append(row3)
                                                                                                                                        T.append(row4)
                                                                                                                                        T.append(row5)
                                                                                                                                        T.append(row6)
                                                                                                                                        T.append(row7)
                                                                                                                                        T.append(row8)
                                                                                                                                        T.append("/")
                                                                                                                                        
                                                                                                                                        #cette commande nous permet de sauvegarder la liste T dans un autre fichier
                                                                                                                                        with open('TS.py', 'wb') as MagicTetrahedra:
                                                                                                                                            pickle.dump(T, MagicTetrahedra)
                                                                                                                                                                                                                                            
                                                                                                                                    #si les entiers ne sont pas tous distincts, on retourne un message d'erreur et le programme prend fin
                                                                                                                                    else:
                                                                                                                                        print("Cannot create a Magic Tetraedron")
                                                                                                                                    #de la même manière, si une des conditions posées sur la stricte supériorité de M par rapport aux sommes des entiers du tétraèdre, on affiche un message d'erreur avant de mettre fin à l'algorithme
                                                                                                                                else:
                                                                                                                                    print("Cannot create a Magic Tetraedron")
                                                                                                                            else:
                                                                                                                                print("Cannot create a Magic Tetraedron")
                                                                                                                        else:
                                                                                                                            print("Cannot create a Magic Tetraedron")
                                                                                                                    else:
                                                                                                                        print("Cannot create a Magic Tetraedron")
                                                                                                                else:
                                                                                                                    print("Cannot create a Magic Tetraedron")
                                                                                                            else:
                                                                                                                print("Cannot create a Magic Tetraedron")
                                                                                                        else:
                                                                                                            print("Cannot create a Magic Tetraedron")
                                                                                                    else:
                                                                                                        print("Cannot create a Magic Tetraedron")
                                                                                                else:
                                                                                                    print("Cannot create a Magic Tetraedron")
                                                                                            else:
                                                                                                print("Cannot create a Magic Tetraedron")
                                                                                        else:
                                                                                            print("Cannot create a Magic Tetraedron")
                                                                                    else:
                                                                                        print("Cannot create a Magic Tetraedron")
                                                                                else:
                                                                                    print("Cannot create a Magic Tetraedron")
                                                                            else:
                                                                                print("Cannot create a Magic Tetraedron")
                                                                        else:
                                                                            print("Cannot create a Magic Tetraedron")
                                                                    else:
                                                                        print("Cannot create a Magic Tetraedron")
                                                                else:
                                                                    print("Cannot create a Magic Tetraedron")
                                                            else:
                                                                print("Cannot create a Magic Tetraedron")
                                                        else:
                                                            print("Cannot create a Magic Tetraedron")
                                                    else:
                                                        print("Cannot create a Magic Tetraedron")
                                                else:
                                                    print("Cannot create a Magic Tetraedron")
                                            else:
                                                print("Cannot create a Magic Tetraedron")
                                        else:
                                            print("Cannot create a Magic Tetraedron")
                                    else:
                                        print("Cannot create a Magic Tetraedron")
                                else:
                                    print("Cannot create a Magic Tetraedron")
                            else:
                                print("Cannot create a Magic Tetraedron")
                        else:
                            print("Cannot create a Magic Tetraedron")
                    else:
                        print("Cannot create a Magic Tetraedron")
                else:
                    print("Cannot create a Magic Tetraedron")
            else:
                print("Cannot create a Magic Tetraedron")
        else:
            print("Cannot create a Magic Tetraedron")
    else:
        print("Cannot create a Magic Tetraedron")

#cette commande nous permet de charger la liste T préalablement enregistrée afin de l'imprimer si nécessaire
with open('TS.py', 'rb') as f:
    T = pickle.load(f)
