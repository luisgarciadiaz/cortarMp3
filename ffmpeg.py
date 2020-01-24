import os
import subprocess
from time import time
clear=lambda:os.system('cls')
clear()
os.chdir('C://Users/luis/Desktop/prueba/')
path='C://Users/luis/Desktop/prueba/'
files =[]
tiempo_inicial=time()
print("empezando a leer archivos")
i=0
for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file:
#files.append(os.path.join(r, file))
            args=("ffprobe","-show_entries", "format=duration","-i",file,'-hide_banner','-loglevel','panic',)
            popen=subprocess.Popen(args,stdout =subprocess.PIPE)
            popen.wait()
            output=popen.stdout.read()
            files.append([file,output])
            i=i+1
numeroArchivos=i
tiempo_final=time()
tiempo_ejecución=tiempo_final-tiempo_inicial
print("terminado de leer archivos tardo:"+str(tiempo_ejecución)+" en segundos un total de "+ str(i))
tiempo_inicial=time()
i=0 
print("empezando a cortar")        
for f in files:
#print(f)
    subprocess.call(['ffmpeg','-y', '-ss','30','-i',f[0],'-t','120','-c','copy',str(i)+f[0],'-hide_banner','-loglevel','panic',])
    i+1
tiempo_final=time()
tiempo_ejecución=tiempo_final-tiempo_inicial
print("terminado de leer archivos tardo:")
print(tiempo_ejecución)
print (" en segundos")
print("listo")