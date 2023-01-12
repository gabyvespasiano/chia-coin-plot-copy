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




discos = ["/media/server/4tb 22/plots","/media/server/4tb 23/plots","/media/server/8 tb2/plots"] ## introducir en orden las ubicaciones de los discos
plots = [19,7,73]## aqui hay que introducir en orden la cantidad de plots faltantes en los discos 
plotsR = []
plotsD = []

for x in plots:
    plotsR.append(0)
    plotsD.append(1)

disco = 0
path = "/media/server/destino/"## aqui introducir donde se estaran generando los plots que deberan ser copiados
x = ""

def copia():
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
	plotsD[tdisco] = 0
	plotsR[disco] = plotsR[disco] + 1
	print("\033[4;35m"+"copia iniciada "+str(tplotsR[tdisco]) +"/"+str(tplots[tdisco])+" en " + tdiscos[tdisco] + " de " + tx)
	os.rename(path+"/"+x, path+"/"+x+"C")
	#os.replace(path+"/"+x, "J:/disco1/"+x)
	shutil.move(path+"/"+x+"C", discos[disco]+"/"+x)
	print("\x1b[1;33m"+"copia termianda "+str(tplotsR[tdisco]) +"/"+str(tplots[tdisco])+" en " + tdiscos[tdisco] + " de " + tx)
	plotsD[tdisco] = 1
	_thread.exit()

plotea = False
while True:
	dir_list = os.listdir(path)

	#print("Files and directories in '", path, "' :")
 
	# prints all files
	for x in dir_list:
		if x.endswith(".plot"):
			#print(x)
			plotea = False
			while plotea == False:		
				#print(disco)			
				if plots[disco] <= plotsR[disco]:
					disco = disco + 1
					if disco >= len(discos):
						disco = 0
				else:
					if plotsD[disco] == 0:
						disco = disco + 1
						if disco >= len(discos):
							disco = 0
						time.sleep(5)
					else:		
						plotea = True
				
			
			_thread.start_new_thread(copia,())

			time.sleep(5)
			disco = disco + 1
			if disco >= len(discos):
				disco = 0
		time.sleep(10)
			
#print(dir_list[0])
	time.sleep(900)
	#if os.path.exists('G:\plots\*.plot'):
	#    print("existe")
