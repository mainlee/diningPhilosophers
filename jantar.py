import _thread as thread
import time, random
import threading

filos = 5
garfo = list()
stats = list() #Status:-1= Sentou, 0 = pensando, 1 = esperando, 2 = comendo
times = list()

for i in range(filos):
   stats.append(0)
   times.append(0)

temp_p = 0.05 #Tempo pensando
temp_c = 0.5 #Tempo comendo 


for i in range(filos):
   garfo.append(threading.Lock())
   #garfo[i].locked()

def filosofo(f):
   ciclos = 0
   f = int(f)

   while True:
      if(stats[f] == -1):
         time.sleep(1)
         stats[f] = 0

      if(stats[f]==0):
         if(garfo[f].locked() == False):
            garfo[f].acquire() #Pega o garfo
            stats[f] = 1 #Esperando
      
      if(stats[f]==1):

         if(garfo[(f+1)%filos].locked() == False):
            garfo[(f+1)%filos].acquire()
            stats[f] = 2 #Comendo
            time.sleep(temp_c) #Tempo comendo
            
            #Solta os garfos e volta a pensar
            garfo[(f+1)%filos].release()
            garfo[f].release()
            stats[f] = 0
            time.sleep(temp_p)
      
      ciclos += 1
      print(f'Ciclo {ciclos}: {stats}')
      if(len(set(stats))==1):
         print(f'Deadlock no ciclo {ciclos}')
         return False


#Inicia o jantar
for i in range(filos):
   print ("Filósofo", i+1, "juntou-se a mesa")
   #ini = time.perf_counter()
   thread.start_new_thread(filosofo, tuple([i]))


while 1: pass