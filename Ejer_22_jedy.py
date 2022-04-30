mochila1=['espada','cuchillo', 'tabla','bolsa','trapo','sable de luz']
#mochila1=['martillo','ddd','gggg']

def usar_la_fuerza(mochila, contador=0): 
    print(mochila[0])
    
    if mochila[0]=='sable de luz':
        return contador
    if (len(mochila)>1):
        mochila.pop(0)
        contador+=1
        return usar_la_fuerza(mochila, contador)
    return -1


cantidad_de_objetos_sacados= usar_la_fuerza(mochila1)
if (cantidad_de_objetos_sacados>=0):
    print('se encontro el sable de luz en la mochila y fue necesario sacar: ', cantidad_de_objetos_sacados,' objetos')
else:
    print('no se encontro el sable de luz en la mochila')

















#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que mas le guste) esta atrapado, pero muy cerca esta su mochila que contiene muchos
#objetos. Implementar una funcion recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden mas objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar
#para encontrarlo;
#c. Utilizar un vector para representar la mochila.