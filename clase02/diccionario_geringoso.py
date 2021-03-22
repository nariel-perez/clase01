#%% 1

###Ejercicio 2.14: diccionario geringoso

def geringoso(cadena):
    new_cadena=''

    for c in cadena:
        if c in 'aeiou':
            new_cadena+= c + 'p' + c 
        else:
                new_cadena+= c    

    return new_cadena     
        


palabras=['banana','manzana', 'mandarina']
dic={}
for i in palabras:
    dic[i]=geringoso(i)


print(dic)

#### output:
##{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}