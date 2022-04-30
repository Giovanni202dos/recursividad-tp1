def conver_numero_romanos( numero_romano):
    dic_romanos={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    if len(numero_romano)==1:
        return dic_romanos[numero_romano]
    else:
        if dic_romanos[numero_romano[0]]>=dic_romanos[numero_romano[1]]:
            return dic_romanos[numero_romano[0]] + conver_numero_romanos(numero_romano[1:])#pasa la subcadena desde la posicion 1 omite la posicion 0
        else:
            return  conver_numero_romanos(numero_romano[1:])- dic_romanos[numero_romano[0]]

numero_romano=input('ingrese el numero romano').upper()#convierte a mayuscula
print(conver_numero_romanos(numero_romano))


    
        