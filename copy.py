#cantidad de plots que entran por disco dependiendo su capacidad
#tb  k32  k33
#2   18   9
#3   36   18
#6   55   27
#8   73   36
#10  91   45
#12  110  55
#14  128  64
#16  146  73
#18  165  82



import os
import shutil
import time
import _thread


discos = ["/media/server/4tb 22/plots","/media/server/4tb 23/plots","/media/server/8 tb2/plots"] # Ubicación de los discos
plots = [19,7,73] # Número de plots faltantes en cada disco 
plotsR = [] # Contador de plots copiados
plotsD = [] # Indicador de estado de copia (0=ocupado, 1=libre)

# Inicializa los contadores y estados de copia
for x in plots:
    plotsR.append(0)
    plotsD.append(1)

disco = 0 # Índice del disco actual
path = "/media/server/destino/" # Directorio de origen de los plots a copiar
x = "" # Nombre del archivo de plot actual

def copia():
	# Variables locales
	global x
	global disco
	global discos
	global plots
	global plotsR
	global plotsD
	tplotsR = plotsR
	tplots = plots
	tx = x
	tdisco = disco
	tdiscos = discos
	
	# Cambia el estado de la copia actual a ocupado
	plotsD[tdisco] = 0
	plotsR[disco] = plotsR[disco] + 1
	
	# Imprime el inicio de la copia
	print("\033[4;35m" + "Copia iniciada " + str(tplotsR[tdisco]) + "/" + str(tplots[tdisco]) + " en " + tdiscos[tdisco] + " de " + tx)
	
	# Realiza la copia renombrándolo primero
	os.rename(path + "/" + x, path + "/" + x + "C")
	shutil.move(path + "/" + x + "C", discos[disco] + "/" + x)
	
	# Imprime la finalización de la copia
	print("\x1b[1;33m" + "Copia terminada " + str(tplotsR[tdisco]) + "/" + str(tplots[tdisco]) + " en " + tdiscos[tdisco] + " de " + tx)
	
	# Cambia el estado de la copia actual a libre
	plotsD[tdisco] = 1
	
	# Sale del hilo
	_thread.exit()

plotea = False

# Bucle infinito
while True:
    dir_list = os.listdir(path)

    # Obtiene la lista de archivos y directorios en el path especificado
    for x in dir_list:
        # Verifica si el archivo termina con ".plot"
        if x.endswith(".plot"):
            plotea = False
            # Busca un disco disponible para copiar el archivo
            while plotea == False:       
                if plots[disco] <= plotsR[disco]:
                    # Si se han copiado todos los archivos posibles en el disco actual, se cambia al siguiente
                    disco = disco + 1
                    if disco >= len(discos):
                        disco = 0
                else:
                    if plotsD[disco] == 0:
                        # Si el disco actual está ocupado, se cambia al siguiente
                        disco = disco + 1
                        if disco >= len(discos):
                            disco = 0
                        time.sleep(5)
                    else:
                        # Si el disco actual está disponible, se puede copiar el archivo
                        plotea = True
                        
            # Inicia una nueva hebra para copiar el archivo
            _thread.start_new_thread(copia,())

            # Espera 5 segundos antes de continuar con la siguiente iteración
            time.sleep(5)
            # Cambia al siguiente disco
            disco = disco + 1
            if disco >= len(discos):
                disco = 0
        # Espera 10 segundos antes de revisar nuevamente la carpeta
        time.sleep(10)
    # Espera 15 minutos antes de revisar nuevamente la carpeta
    time.sleep(900)
