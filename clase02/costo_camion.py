####CLASE 02####

#%% 1 Ejercicio 2.8 y 2.9 : Lectura de un archivo de datos
########################### modificado para usar el modulo csv
import csv


def costo_camion(nombre_archivo):
    total=0.0
    f=open('../Data/'+str(nombre_archivo))
    rows=csv.reader(f)
    header=next(rows)
    header
    for row in rows:
        try:
            #rows=csv.reader(f)
            row0=row[0]
            row1=row[1]
            row2=row[2]
            if row1=='' or row2=='':
                    raise ValueError('valor faltante')
            total+=int(row1)*float(row2)
           
        except ValueError:
            print(f'Warning:datos faltantes para {row0}')
    #print(total)
    print(f'Costo total {total:.2f} ')    
    f.close()



costo_camion('camion.csv')


    
