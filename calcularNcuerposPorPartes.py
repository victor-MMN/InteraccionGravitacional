

# Librerias :

import sys # Paquete para usar el comando exit() que permite detener el programa en esa linea.
import numpy as np 
import os # Paquete para crear un archivo.
import time # Paqueteria para calcular el tiempo de ejecucion.
import math # Paqueteria para redondear numeros.
import random as rd # Pqueteria para general numeros aleatorios.
import PySimpleGUI as sg # Paqueteria para crear una ventana emergente.




# Funciones :


def acceleraciones(t, r, m):


    # Inicializamos vector donde se guardaran las acceleraciones, r tiene las coordenadas de los n cuerpos.

    a = np.zeros(len(r),np.longdouble) 

    # Calculamos la interaccion gravitacional entre los n cuerpos.

    # print("m : " + str(len(m)))

    i,j = 0,0

    while (i < len(m)): # Ciclo para obtener la aceleracion del cuerpo i.

        # print("i = " + str(i))


        while (j < len(m)): # Ciclo donde se sumaran las interacciones entre el cuerpo i y los cuerpos j's.



            if ((i == (len(m)-1)) and (i == j)): # Condicion para terminar los ciclos, si ya llegamos al
                                                 # ultimo cuerpo y a la ultima interaccion.

                break

            elif (i == j): # Condicion para evitar calcular la interaccion del cuerpo i con el mismo.

                j += 1

            # print("j = " + str(j))

            # Ecuacion de la interaccion gravitacional por unidad de masa i.


            a[3*i:3*i+3] += -G * m[j] * (r[3*i:3*i+3] - r[3*j:3*j+3]) / (np.linalg.norm(r[3*i:3*i+3] - r[3*j:3*j+3])**3 + epsilon)


            j += 1
            


        i += 1
        j = 0
        
        

    return a


# def acceleraciones(t, r, m):


#     # Inicializamos vector donde se guardaran las acceleraciones, r tiene las coordenadas de los n cuerpos.

#     a = np.zeros(len(r),np.longdouble) 

#     # Calculamos la interaccion gravitacional entre los n cuerpos.

#     # print("m : " + str(len(m)))

#     for i in range(len(m)) : # Ciclo para obtener la aceleracion del cuerpo i.

#         # print("i = " + str(i))


#         for j in range(len(m)-1) : # Ciclo donde se sumaran las interacciones entre el cuerpo i y los cuerpos j's.

            

#             if ((i == (len(m)-1)) and (i == j)): # Condicion para terminar los ciclos, si ya llegamos al
#                                                  # ultimo cuerpo y a la ultima interaccion.

#                 break

#             elif (i == j): # Condicion para evitar calcular la interaccion del cuerpo i con el mismo.

#                 j += 1

#             # print("j = " + str(j))

#             # Ecuacion de la interaccion gravitacional por unidad de masa i.


#             a[3*i:3*i+3] += -G * m[j] * (r[3*i:3*i+3] - r[3*j:3*j+3]) / (np.linalg.norm(r[3*i:3*i+3] - r[3*j:3*j+3])**3 + epsilon)

#     return a



def cuerposAleatorios(masaCuerpos, numCuerpos) :

    mAlt = np.array([masaCuerpos])
    rAlt = np.array([rd.uniform(-1,1), rd.uniform(-1,1), rd.uniform(-1,1)])
    vAlt = np.array([rd.uniform(-1,1), rd.uniform(-1,1), rd.uniform(-1,1)])

    for i in range(numCuerpos-1) :

        rAlt = np.concatenate((rAlt, [rd.uniform(-1,1), rd.uniform(-1,1), rd.uniform(-1,1)]))
        vAlt = np.concatenate((vAlt, [rd.uniform(-1,1), rd.uniform(-1,1), rd.uniform(-1,1)]))
        mAlt = np.concatenate((mAlt, [masaCuerpos]))

    return mAlt, rAlt, vAlt*0.1

# def cuerposAleatorios(masaCuerpos, numCuerpos) :

#     mAlt = np.array([masaCuerpos])
#     rAlt = np.array([rd.random() - 1, rd.random() - 1, rd.random() - 1])
#     vAlt = np.array([rd.random() - 1, rd.random() - 1, rd.random() - 1])

#     for i in range(numCuerpos-1) :

#         rAlt = np.concatenate((rAlt, [rd.random(), rd.random(), rd.random()]))
#         vAlt = np.concatenate((vAlt, [rd.random(), rd.random(), rd.random()]))
#         mAlt = np.concatenate((mAlt, [masaCuerpos]))

#     return mAlt, rAlt, vAlt*0.1








# Condiciones iniciales :



epsilon = 0 # Factor de suavizado, se usa en la aceleracion para evitar el 0 de la maquina.


# Constantes y nombre de carpeta.


G = 1 
Gc = 6.6743e-11
c = 2.9979e8

# Factores de convercion de unidades.

# unidadMasa =  float(9.22482e-27) # kg
unidadDistancia = float(0.378e9) # m
unidadTiempo = float(86400) # s


# carpeta = "tesis\muchosCuerpos"
carpeta = "tesis\cuerpos3"


# Tiempo de simulacion. 

t0 = 0 / unidadTiempo
# tf = 10 * 27.3217 * 24 * 60 * 60 / unidadTiempo
tf = 10 * 365 * 24 * 60 * 60 / unidadTiempo 
# tf = 1 * 1 * 24 * 60 * 60 / unidadTiempo 
N = 512000
# N = 140 * 2**13
dt = (tf - t0)/N 
# print(dt)
# print(dt**4)


# Sol.

m1 = 1988500e24 * (Gc *  unidadTiempo**2 / unidadDistancia**3)

x0_1 = 0 / unidadDistancia
y0_1 = 0 / unidadDistancia
z0_1 = 0 / unidadDistancia

vx0_1 = 0 * (unidadTiempo/unidadDistancia)
vy0_1 = 0 * (unidadTiempo/unidadDistancia)
vz0_1 = 0 * (unidadTiempo/unidadDistancia)

p1_0 = np.array([x0_1, y0_1, z0_1], np.longdouble)
v1_0 = np.array([vx0_1, vy0_1, vz0_1], np.longdouble)



# Mercurio en el apogeo al sol. 


m2 = 0.3301e24 * (Gc * unidadTiempo**2 / unidadDistancia**3)

x0_2 = 69.818e9 / unidadDistancia
y0_2 = 0 / unidadDistancia
z0_2 = 0 / unidadDistancia

vx0_2 = 0 * (unidadTiempo/unidadDistancia)
vy0_2 = 38.86e3 * (unidadTiempo/unidadDistancia)
vz0_2 = 0 * (unidadTiempo/unidadDistancia)

p2_0 = np.array([x0_2, y0_2, z0_2], np.longdouble)
v2_0 = np.array([vz0_2, vy0_2, vz0_2], np.longdouble) 




# Venus en el apogeo al sol. 


m3 = 4.8673e24 * (Gc * unidadTiempo**2 / unidadDistancia**3)

x0_3 = 108.941e9 / unidadDistancia
y0_3 = 0 / unidadDistancia
z0_3 = 0 / unidadDistancia

vx0_3 = 0 * (unidadTiempo/unidadDistancia)
vy0_3 = 34.79e3 * (unidadTiempo/unidadDistancia)
vz0_3 = 0 * (unidadTiempo/unidadDistancia)

p3_0 = np.array([x0_3, y0_3, z0_3], np.longdouble)
v3_0 = np.array([vz0_3, vy0_3, vz0_3], np.longdouble) 




# Tierra en el apogeo al sol. 


m4 = 5.9722e24 * (Gc * unidadTiempo**2 / unidadDistancia**3) 

x0_4 = 152.1e9 / unidadDistancia
# x0_4 = 0 / unidadDistancia
y0_4 = 0 / unidadDistancia
z0_4 = 0 / unidadDistancia

vx0_4 = 0 * (unidadTiempo/unidadDistancia)
vy0_4 = 29.29e3 * (unidadTiempo/unidadDistancia)
# vy0_4 = 0 * (unidadTiempo/unidadDistancia)
vz0_4 = 0 * (unidadTiempo/unidadDistancia)

p4_0 = np.array([x0_4, y0_4, z0_4], np.longdouble)
v4_0 = np.array([vx0_4, vy0_4, vz0_4], np.longdouble) 



# Luna en el apogeo a la tierra. 


m41 = 0.07346e24 * (Gc * unidadTiempo**2 / unidadDistancia**3) 

x0_41 = (152.1e9 + 0.4055e9) / unidadDistancia
# x0_41 = 0.4055e9 / unidadDistancia 
y0_41 = 0 / unidadDistancia
z0_41 = 0 / unidadDistancia

vx0_41 = 0 * (unidadTiempo/unidadDistancia)
vy0_41 = (29.29e3 + 0.97e3) * (unidadTiempo/unidadDistancia)
# vy0_41 = 0.97e3 * (unidadTiempo/unidadDistancia)
vz0_41 = 0 * (unidadTiempo/unidadDistancia)

p41_0 = np.array([x0_41, y0_41, z0_41], np.longdouble)
v41_0 = np.array([vx0_41, vy0_41, vz0_41], np.longdouble) 




# Marte en el apogeo al sol. 


m5 = 0.64169e24 * (Gc * unidadTiempo**2 / unidadDistancia**3)

x0_5 = 249.261e9 / unidadDistancia
y0_5 = 0 / unidadDistancia
z0_5 = 0 / unidadDistancia

vx0_5 = 0 * (unidadTiempo/unidadDistancia)
vy0_5 = 21.97e3 * (unidadTiempo/unidadDistancia)
vz0_5 = 0 * (unidadTiempo/unidadDistancia)

p5_0 = np.array([x0_5, y0_5, z0_5], np.longdouble)
v5_0 = np.array([vz0_5, vy0_5, vz0_5], np.longdouble) 







# Jupiter en el apogeo al sol. 


m6 = 1898.13e24 * (Gc * unidadTiempo**2 / unidadDistancia**3)

x0_6 = 816.363e9 / unidadDistancia
y0_6 = 0 / unidadDistancia
z0_6 = 0 / unidadDistancia

vx0_6 = 0 * (unidadTiempo/unidadDistancia)
vy0_6 = 12.44e3 * (unidadTiempo/unidadDistancia)
vz0_6 = 0 * (unidadTiempo/unidadDistancia)

p6_0 = np.array([x0_6, y0_6, z0_6], np.longdouble)
v6_0 = np.array([vz0_6, vy0_6, vz0_6], np.longdouble) 








# Saturno en el apogeo al sol. 


m7 = 568.32e24 * (Gc * unidadTiempo**2 / unidadDistancia**3)

x0_7 = 1506.527e9 / unidadDistancia
y0_7 = 0 / unidadDistancia
z0_7 = 0 / unidadDistancia

vx0_7 = 0 * (unidadTiempo/unidadDistancia)
vy0_7 = 9.09e3 * (unidadTiempo/unidadDistancia)
vz0_7 = 0 * (unidadTiempo/unidadDistancia)

p7_0 = np.array([x0_7, y0_7, z0_7], np.longdouble)
v7_0 = np.array([vz0_7, vy0_7, vz0_7], np.longdouble) 











# Urano en el apogeo al sol. 


m8 = 86.811e24 * (Gc * unidadTiempo**2 / unidadDistancia**3)

x0_8 = 3001.390e9 / unidadDistancia
y0_8 = 0 / unidadDistancia
z0_8 = 0 / unidadDistancia

vx0_8 = 0 * (unidadTiempo/unidadDistancia)
vy0_8 = 6.49e3 * (unidadTiempo/unidadDistancia)
vz0_8 = 0 * (unidadTiempo/unidadDistancia)

p8_0 = np.array([x0_8, y0_8, z0_8], np.longdouble)
v8_0 = np.array([vz0_8, vy0_8, vz0_8], np.longdouble) 











# Neptuno en el apogeo al sol. 


m9 = 102.409e24 * (Gc * unidadTiempo**2 / unidadDistancia**3)

x0_9 = 4558.857e9 / unidadDistancia
y0_9 = 0 / unidadDistancia
z0_9 = 0 / unidadDistancia

vx0_9 = 0 * (unidadTiempo/unidadDistancia)
vy0_9 = 5.37e3 * (unidadTiempo/unidadDistancia)
vz0_9 = 0 * (unidadTiempo/unidadDistancia)

p9_0 = np.array([x0_9, y0_9, z0_9], np.longdouble)
v9_0 = np.array([vz0_9, vy0_9, vz0_9], np.longdouble) 













# Arreglos con las cantidades de los cuerpos.

# m = np.array([m4, m41])
# r0 = np.concatenate((p4_0, p41_0), dtype = np.longdouble)
# v0 = np.concatenate((v4_0, v41_0), dtype = np.longdouble)
# nomCuerpos = ('Tierra', 'Luna')
# planetas = 'TL'

m = np.array([m1, m4, m41])
r0 = np.concatenate((p1_0, p4_0, p41_0), dtype = np.longdouble)
v0 = np.concatenate((v1_0, v4_0, v41_0), dtype = np.longdouble)
nomCuerpos = ('Sol', 'Tierra', 'Luna')
planetas = 'STL'



# m = np.array([m1, m2, m3, m4, m41, m5, m6, m7, m8, m9])
# r0 = np.concatenate((p1_0, p2_0, p3_0, p4_0, p41_0, p5_0, p6_0, p7_0, p8_0, p9_0))
# v0 = np.concatenate((v1_0, v2_0, v3_0, v4_0, v41_0, v5_0, v6_0, v7_0, v8_0, v9_0))
# nomCuerpos = ('Sol', 'Mercurio', 'Venus','Tierra', 'Luna', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno')
# planetas = 'TODOS'

# # m = np.array([m1, m4, m41, m9])
# # r0 = np.concatenate((p1_0, p4_0, p41_0, p9_0))
# # v0 = np.concatenate((v1_0, v4_0, v41_0, v9_0))
# # nomCuerpos = ('Sol','Tierra', 'Luna', 'Nepturno')
# # planetas = 'STLN'


# rd.seed(9)
# masaC = 5
# numC = 3
# m,r0,v0 = cuerposAleatorios(masaC, numC)

# print(m[0], r0[0:3], v0[0:3])
# print(m[1], r0[3:6], v0[3:6])
# print(m[2], r0[6:9], v0[6:9])
# print(m[3], r0[10:13], v0[10:13])
# print(m[4], r0[13:16], v0[13:16])
  

# sys.exit()








print("Calculando posiciones y escribiendolas en el archivo...")

st = time.time() # Tiempo inicial.


# Calculo de la trayectoria con RK orden 4 para n cuerpos en 3D.

nombre = f"{planetas}_RK4_dt={dt}_N={N}" # Sistema.
# nombre = f"{numC}_m={masaC}_RK4_dt={dt}_N={N}" # Cuerpos aleatorios.




# Las trayectorias de los cuerpos los separaremos en diferentes archivos, partes = 1,2,3,..
# esto lo haremos para los casos donde llenamos los archivos con nuestros datos o por si no 
# queremos tener archivos muy pesados. Usaremos dos variables :
#
#  parte : Identificara que parte de la trayectoria esta guardada en el archivo, ademas nos ayudara
#          en la condicion de salida de la escritura de archivos (se usa en el for de abajo).
#  numDatos : Sera la cantidad de datos que se guardaran en cada archivo. 
#  tfParte : Intervalo de tiempo que se guardara en cada parte.
#  partesTotales : Numero de partes totales.


numDatos = 1000000


# Vemos cuanto valdra el intervalo, si N < numDatos entonces solo necesitaremos un archivo por lo tanto
# el intervalo sera todo el tiempo tfParte = tf.
# Si los puntos totales son mas que los puntos requeridos en cada parte entonces dividimos el tiempo total en
# la cantidad de partes que se necesite, redondeando el valor hacia arriba para que todos los datos esten 
# guardados en un archivo.


if (N/numDatos <= 1) :

    partesTotales = 1
    tfParte = tf
else :
    partesTotales = math.ceil(N/numDatos)
    tfParte = tf /  partesTotales



# Inicializamos los vector donde se guardaran los valores a graficar.

t = t0
r = r0
v = v0
     

for parte in range(1, 1 + partesTotales) : # el + 1 es por como funciona la funcion range.

    # Creamos archivo para guardar el tiempo y posiciones, si ya existe lo remplaza.
    with open(f"datos\{carpeta}\POS_{nombre}_P{parte}De{partesTotales}.txt", 'w') as posFile:

        # Creamos archivo para guardar el tiempo y velocidades, si ya existe lo remplaza.
        with open(f"datos\{carpeta}\VEL_{nombre}_P{parte}De{partesTotales}.txt", 'w') as velFile: 

            # Nombres de las columnas.

            posFile.write("Tiempo     ")
            velFile.write("Tiempo     ")


            # Cuerpos aleatorios :

            # posFile.write(f"Posicones de {len(m)} cuerpos: ") 
            # velFile.write(f"Velocidades de {len(m)} cuerpos: ") 


            # Sistemas :

            for j in range(len(m)) :
                
                posFile.write(nomCuerpos[j]  + "(x,y,z)     ")    
                velFile.write(nomCuerpos[j]  + "(x,y,z)     ") 



            posFile.write(f"Posiciones de los {len(m)} cuerpos") 
            velFile.write(f"Velocidades de los {len(m)} cuerpos") 
            posFile.write(os.linesep)
            velFile.write(os.linesep)
                    
            posFile.write(" " + os.linesep)
            velFile.write(" " + os.linesep)



            # npunto nos indica en el valor de N que nos quedamos en el archivo anterior, que es numDatos por
            # la parte de archivo donde estamos, ponemos parte - 1 porque en el for loop de la escritura
            # empezamos con parte = 1.

            npunto = numDatos * (parte - 1)

            # Restamos parte en el valor final porque al cambiar de archivo el ultimo punto se escribe en el 
            # archivo que esta y en el siguiente, esto pasara cada vez que cambiemos de arhivo por lo tanto
            # restaremos esos valores repetidos al valor final. Le restamos 1 a parte porque empieza en 1.

            for puntos in range( npunto, N - (parte-1) ) : 
                
            # while (True) :


                # Escribiendo las posiciones en el archivo.


                posFile.write(str(t)  + "       ") # Tiempo.
                velFile.write(str(t)  + "       ") # Tiempo.

                for j in range(3*len(m)) :

                    posFile.write(str(r[j])  + "       ") # Posiciones.
                    velFile.write(str(v[j])  + "       ") # Velocidades.

                posFile.write(os.linesep)
                velFile.write(os.linesep)



                # Calculando la dinamica de los N cuerpos.

                # RK Orden 4 para la velocidad y la posicion:

                # r += dt*v
                # Kiv : k's de la velocidad.
                # Kir : k's de la posicion.

                k1v = dt*acceleraciones(t, r, m)
                k1r = dt*v

                k2v = dt*acceleraciones(t + dt/2, r + k1r/2, m)
                k2r = dt*(v + k1v/2)

                k3v = dt*acceleraciones(t + dt/2, r + k2r/2, m)
                k3r = dt*(v + k2v/2)

                k4v = dt*acceleraciones(t + dt, r + k3r, m)
                k4r = dt*(v + k3v)

                r += (k1r + 2*k2r + 2*k3r + k4r)/6
                v += (k1v + 2*k2v + 2*k3v + k4v)/6

                t += dt



                # Condicion para que pare el ciclo while.
                # En general se parara cuando el tiempo t sobrepase el tiempo correspondiente a la particion parte.
                # El tiempo de cada particion es el intervalo de tiempo que tendra cada particion tfParte por la
                # particion parte, t empezara en la siguiente particion ya con el valor correspondiente a esa parte.
                # Si por el error numero tenemos que tfParte * la ultima parte es mayor que tf tenemos la siguiente
                # condicion de paro t > tf.

                # if ((t > tfParte * parte) or (t > tf)) :

                #     break

                # Condicion para cambio de archivo.
                # Para cambiar de archivo la variable iterada (puntos )debe ser igual al numero de datos por archivo
                # (numDatos) por la parte donde estamos (parte).

                if (puntos == numDatos*parte) :

                    break
                

    





et = time.time() # Tiempo final.

tiempo = et - st # Tiempo de ejecucion.

print(f"Archivo : {nombre}   tiene {partesTotales} partes.")

print('Tiempo de ejecucion:', time.strftime("%H:%M:%S", time.gmtime(tiempo)))

# sg.popup('Ya se termino de ejecutar el codigo, ponte vergas.')









# # Contar el numero de vueltas de cada cuerpo.


# print("Calculando Revoluciones de cada cuerpo...")



# for j in range(len(m)): # j-esimo cuerpo en la coordenada y. 

#     revoluciones = 0 
#     i = 1 # contador para cada i-esimo instante de tiempo.

#     while (i < len(t)):             # En este ciclo vemos cuando el cuerpo en el instante i-1 de la coordenada
#                                     # y del cuerpo es un numero negativo y en el instante despues i que sea
#                                     # positiva. Esto significaria que el cuerpo paso por el eje x positivo.
#         if (r[i-1, 3*j + 1] < 0):

#             if (r[i, 3*j + 1] > 0):

#                 revoluciones += 1

#         i += 1


#     print("Revoluciones del cuerpo " + str(j + 1) + " : " + str(revoluciones))


# et = time.time() # Tiempo final.

# tiempo = et - st # Tiempo de ejecucion.

# print('Tiempo de ejecucion:', time.strftime("%H:%M:%S", time.gmtime(tiempo)))
