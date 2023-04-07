

# Librerias :

import sys # Paquete para usar el comando exit() que permite detener el programa en esa linea.
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D # Paqueteria para los ejes 3D.
from matplotlib import animation # Paqueteria para la animacion.
import pandas as pd # Paquete que usare para leer archivos.
import time # Paqueteria para calcular el tiempo de ejecucion.
import math # Paqueteria para redondear numeros.
import dask.dataframe as dd # Paqueteria para trabajar con dataframes con demasiados datos.



# Funciones.

def nBodies_Animation3D(num,fps,time,Bodies,data,nameBodies,colorBodies):


    ax.clear()  # Limpia la figura para actualizar la linea, puntos, titulo y ejes. 


    # print(fps * num)


    j = 0

    while j < (Bodies): # While para plotear las trayectorias de las diferentes masas.

        # loc crea un dataframe del existente. to.numpy para convertir dataframe de panda a array de numpy.
        # loc es inclusivo con los indeces. 
        rg = data.loc[:, 1 + 3*j : 3*j + 3].astype(float).to_numpy()


        # Actualizar linea de trayectoria (num+1 debido a como funcionan los indices en python).
        # fps * num seria dibujar cada fps plots, esto accelera la animacion si son demasiados puntos.

        ax.plot3D(rg[:(fps * num)+1, 0], rg[:(fps * num)+1, 1], rg[:(fps * num)+1, 2], \
                        linewidth=2, color = colorBodies[j])



        # Actualizar punto final.

        # ax.scatter(rg[(fps * num), 0], rg[(fps * num), 1], rg[(fps * num), 2], \
        #             marker='o', s=1, label = nameBodies[j], color = colorBodies[j])

        ax.scatter(rg[(fps * num), 0], rg[(fps * num), 1], rg[(fps * num), 2], \
                    marker='o', s=20, color = colorBodies[j])

        j += 1


        # Origen constante.

        # ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0], marker='o') 






    # Limites de los ejes (opcional).
    # Le pongo +- 10 por si las orbitas estan en un plano, si estan por ejemplo en el plano x,y entonces
    # los limites de z serian de (0,0) lo cual no se puede graficar.

    # if (np.amin(rg[:, 0 :: 3]) == np.amax(rg[:, 0 :: 3])) : # Vemos si esta en el plano y,z.

    #     ax.set_xlim3d([-10, 10])
    #     ax.set_ylim3d([np.amin(rg[:, 1 :: 3]), np.amax(rg[:, 1 :: 3])])
    #     ax.set_zlim3d([np.amin(rg[:, 2 :: 3]), np.amax(rg[:, 2 :: 3])])

    # elif (np.amin(rg[:, 1 :: 3]) == np.amax(rg[:, 1 :: 3])) : # Vemos si esta en el plano x,z.

    #     ax.set_xlim3d([np.amin(rg[:, 0 :: 3]), np.amax(rg[:, 0 :: 3])])
    #     ax.set_ylim3d([-10, 10])
    #     ax.set_zlim3d([np.amin(rg[:, 2 :: 3]), np.amax(rg[:, 2 :: 3])])

    # elif (np.amin(rg[:, 2 :: 3]) == np.amax(rg[:, 2 :: 3])) : # Vemos si esta en el plano x,y.

    #     ax.set_xlim3d([np.amin(rg[:, 0 :: 3]), np.amax(rg[:, 0 :: 3])])
    #     ax.set_ylim3d([np.amin(rg[:, 1 :: 3]), np.amax(rg[:, 1 :: 3])])
    #     ax.set_zlim3d([-10, 10])
    # else : # No esta en uno de los planos principales, ninguna coordenada es 0 en toda la trayectoria.

    #     ax.set_xlim3d([np.amin(rg[:, 0 :: 3]), np.amax(rg[:, 0 :: 3])])
    #     ax.set_ylim3d([np.amin(rg[:, 1 :: 3]), np.amax(rg[:, 1 :: 3])])
    #     ax.set_zlim3d([np.amin(rg[:, 2 :: 3]), np.amax(rg[:, 2 :: 3])])


    # Etiquetas de la grafica.

    ax.set_title('Tiempo = ' + str(format(time[fps * num],".4g")) + ' D', fontsize = 17)
    # ax.set_title('Trayectorias')
    ax.set_xlabel(r'$x$ $(M_l)$', fontsize = 10)
    ax.set_ylabel(r'$y$ $(M_l)$', fontsize = 10)
    ax.set_zlabel(r'$z$ $(M_l)$', fontsize = 10)
    # ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=3)

    # Removemos grid, ejes o ticks.
    # plt.grid(False)
    # plt.axis('off')
    # ax.set_xticklabels([])
    # ax.set_yticklabels([])
    # ax.set_zticklabels([])





# Leer archivo.

print("Leyendo el archivo y graficandolo...")
st = time.time() # Tiempo inicial.


# nameFile = input("Nombre del archivo : ")




m = 5
folder = "tesis\muchosCuerpos"
# folder = "tesis\cuerpos3"
nameFile = "5_m=5_RK4_dt=8.719308035714285e-07_N=1146880" 
N = 1146880
totalParts = 2


# nameBodies = ('Sol', 'Tierra', 'Luna')
# colorBodies = ('orange', 'blue', 'gray')

# nameBodies = ('Sol', 'Mercurio', 'Venus','Tierra', 'Luna', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno')
# colorBodies = ('orange', 'brown', 'gold', 'blue', 'gray', 'red', 'navajowhite', 'yellow', 'aqua', 'navy')

# # nameBodies = ('Sol','Tierra', 'Luna', 'Neptuno')
# colorBodies = ('orange', 'blue', 'gray', 'navy')

nameBodies = ('1', '2', '3','4', '5')
colorBodies = ('orange', 'navy', 'red', 'blue', 'gray')


part = tuple(i for i in range(1,1 + totalParts))
dir = (folder, nameFile, totalParts, part)



# Graficando.

fig = plt.figure(figsize=(12, 12), dpi = 180) # figsize : pulgada por pulgada.
                                            # dpi : puntos por pulgada (resolucion).
ax = plt.axes(projection='3d')
# ax = plt.axes()
ax.set_xlabel(r'$x$ $(M_l)$')
ax.set_ylabel(r'$y$ $(M_l)$')
ax.set_zlabel(r'$z$ $(M_l)$')

# startx, endx = ax.get_xlim()
# ax.xaxis.set_ticks(np.arange(startx - 1, endx + 1.1, 0.5))

# starty, endy = ax.get_ylim()
# ax.yaxis.set_ticks(np.arange(startx - 1, endx + 1.1, 0.5))

# startz, endz = ax.get_zlim()
# ax.zaxis.set_ticks(np.arange(startx - 1, endx + 1.1, 0.5))



zoom = "ext"
# zoom = "int"
# ax.set_xlim3d([399, 404])
# ax.set_ylim3d([-30, 30])
# ax.set_xlim3d([-400, 400])
# ax.set_ylim3d([-400, 400])
# ax.set_xlim3d([-1, 1])
# ax.set_ylim3d([-1, 1])
# ax.set_zlim3d([-1, 1])

# Cambiamos la camara al momento de ver por primera vez el plot y cuando se guarda.
# El primer numero indica los grados con respecto al eje z+ y el segundo con el eje x+

# ax.view_init(30, 310) 
ax.view_init(80, 270) 


for part in range(1, 1 + totalParts) : # el + 1 es por como funciona la funcion range.





    # Primer argumento es el nombre del archivo a leer.
    #
    # sep : el formato de separacion entre los datos \s+ significa que es una cantidad de espacios.
    #
    # header : Si tomaremos algun titulo para las columnas para poner en el dataframe.
    #
    # skiprows : Cuantas columnas se saltaran para empezar a leer.
    #
    # dtype : Tipo de datos a leer.


    data = pd.read_csv(f"datos\{folder}\POS_{nameFile}_P{part}De{totalParts}.txt",sep='\s+', \
                        header=None, skiprows = 1, dtype = 'float')            
    data = pd.DataFrame(data)

    


    for j in range(m): # While para plotear las trayectorias de las diferentes masas.

        # loc crea un dataframe del existente. to.numpy para convertir dataframe de panda a array de numpy.
        # 1 + al principio porque la primera columna es el tiempo.

        rg = data.loc[:, 1 + (3*j) : 1 + (3*j + 3)].astype(float).to_numpy()
    

        # ax.plot3D(rg[:, 0], rg[:, 1], rg[:, 2], color = colorBodies[j]) # Sistema.
        ax.plot3D(rg[:, 0], rg[:, 1], rg[:, 2]) # Cuerpos aleatorios.


        if (part == totalParts) :


            # Sistema :

            # ax.scatter(rg[(len(rg) - 1), 0], rg[(len(rg) - 1), 1], rg[(len(rg) - 1), 2], \
                            # marker='o', label = nameBodies[j], color = colorBodies[j])
            # ax.scatter(rg[(len(rg) - 1), 0], rg[(len(rg) - 1), 1], rg[(len(rg) - 1), 2], \
            #             marker='o', color = colorBodies[j])

            # Cuerpos aleatorios :

            ax.scatter(rg[(len(rg) - 1), 0], rg[(len(rg) - 1), 1], rg[(len(rg) - 1), 2], \
                        marker='o')





# Colocar las legendas de las graficas.
# loc : Pone las leyendas en la parte del plot que indiques.
# bbox_to_anchor : Si las leyendas quedan encimadas con el plot, con esto podemos sacarlas (x,y)
# ncol : Especificamos el numero de columnas que tendra la legenda donde estaran los nombres de los plots.

# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=4)

plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))

# Guardar plot.
plt.savefig(f"graficas\{folder}\{nameFile}_{zoom}.pdf", bbox_inches="tight", pad_inches = 0) 


# plt.show()
plt.close()



et = time.time() # Tiempo final.

tiempo = et - st # Tiempo de ejecucion.

print('Tiempo de ejecucion:', time.strftime("%H:%M:%S", time.gmtime(tiempo)))








# Graficamos la animacion.

print("Realizando la animacion...")

st = time.time() # Tiempo inicial.

fig = plt.figure(figsize=(5, 6), dpi = 120) # figsize : pulgada por pulgada, 
                                            #dpi : puntos por pulgada (resolucion).

ax = plt.axes(projection='3d')

# Quitamos algo del espacio en blanco del plot.
fig.subplots_adjust(left=-0.05, bottom=-0.05, right=0.95, top=0.95, wspace=None, hspace=None)
# fig.subplots_adjust(wspace=None, hspace=None)
# fig.subplots_adjust(left=0, bottom=0, right=1, top=1)


# Movemos la vista del plot.
# ax.view_init(80, 270) 
ax.view_init(30, 310) 




# Creamos un data frame donde este la infromacion de todos los archivos en uno solo.

for part in range(1, 1 + totalParts) : # el + 1 es por como funciona la funcion range.


    # Primer argumento es el nombre del archivo a leer.
    #
    # sep : el formato de separacion entre los datos \s+ significa que es una cantidad de espacios.
    #
    # header : Si tomaremos algun titulo para las columnas para poner en el dataframe.
    #
    # skiprows : Cuantas columnas se saltaran para empezar a leer.
    #
    # dtype : Tipo de datos a leer.


    if part == 1 :

        finalDataAnimation = pd.read_csv(f"datos\{folder}\POS_{nameFile}_P{part}De{totalParts}.txt",sep='\s+', \
                        header=None, skiprows = 1, dtype = 'float')            
        finalDataAnimation = pd.DataFrame(finalDataAnimation)
        # print(finalDataAnimation.shape)

    else :

        dataAnimation = pd.read_csv(f"datos\{folder}\POS_{nameFile}_P{part}De{totalParts}.txt",sep='\s+', \
                        header=None, skiprows = 1, dtype = 'float')            
        dataAnimation = pd.DataFrame(dataAnimation)
        # print(dataAnimation.shape)

        # axis = 0 concatena por fila y = 1 por columna. 
        # ignore_index=True hace que los indices esten corridos.
        finalDataAnimation = pd.concat([finalDataAnimation, dataAnimation], axis=0, ignore_index=True)


# print(finalDataAnimation.shape)

# sys.exit()




# Elegimos que cuerpos y hasta que tiempo los vamos a graficar

# times = finalDataAnimation.loc[:64000, 0]
# positions = finalDataAnimation.loc[:64000, 1:]
times = finalDataAnimation.loc[:, 0]
positions = finalDataAnimation.loc[:, 1:]

# print(times.shape)
# print(positions.shape)
# print(times.astype(float).to_numpy()[1])
# print(positions.astype(float).to_numpy()[:, 1:3])


# sys.exit()




# Llamamos a la funcion para la animacion.

# fig : Canvas.
# nBodies_Animation3D : Funcion que va ploteando cada frame.

# fargs : Argumentos de la funcion donde se plotea, en este caso nBodies_Animation3D, esta funcion
# no puede llevar ningun argumento, aunque este definida con un argemnto ese es una varible iterativa que
# la propia funcion animation.FuncAnimation usa para graficar todos los frames.

# interval : tiempo en milisegundos entre cada frame.

# frames : Numero de plots que se usaran en la animacion, si quieres que salga toda la trayectoria o grafica
# que tienes, debes de poner que sea igual al numero de plots que se pintaran en toda la animacion.

# Cuando la animacion tiene demasiados puntos tarda mucho en verse la evolucion de la animacion. Por ello
# En lugar de graficar los puntos 1 por 1, graficamos cada fps puntos.



fps = 1080*5

numPoints = int(len(times)/fps)
# print(len(times))
# print(numPoints)


# sys.exit()

# Argumentos de fargs : (num,fps,time,bodies,data,nameBodies,colorBodies)

animacion = animation.FuncAnimation(fig, nBodies_Animation3D, \
                                    fargs=(fps, times, m, positions, nameBodies, colorBodies), \
                                    interval = 60, frames = numPoints)




# Guardar animacion.

# f = r"C:\Users\Victor Minjares\OneDrive\Escritorio\escuela\programacion\VScode_git\NCuerpos.py\3cuerpos.gif"
writergif = animation.PillowWriter(fps= fps) #  Funcion que escribira la animacion a guardar.
# animacion.save(f"graficas\{folder}\{nameFile}.gif", writer=writergif) 
animacion.save(f"{nameFile}.gif", writer=writergif) 



et = time.time() # Tiempo final.

tiempo = et - st # Tiempo de ejecucion.

print('Tiempo de ejecucion:', time.strftime("%H:%M:%S", time.gmtime(tiempo)))

# plt.show()
plt.close()
