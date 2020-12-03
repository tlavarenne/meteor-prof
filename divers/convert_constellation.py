import matplotlib.pyplot as plt
import numpy as np
f = open("binarymeteor2.s","rb")
soft_bits = np.fromfile(f,dtype = np.int8)

#soft_bits=soft_bits[len(soft_bits)//2:len(soft_bits)//2+50*16384] #Si le fichier complet est trop gros on en sélectionne une partie



'''
1 :
1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0

2:
0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,1,0,1,1

3:
1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,1

4:
0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,1,0

5:
1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0

6:
0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1,1,1

7:
1,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,0,1

8:
0,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0

'''
#################################################################################
constellation=7   #Choisir le numéro après avoir effectué test_constellation.py
#################################################################################

if constellation == 1:   #on ne fait rien
	pass
	
if constellation == 2:      #On inverse tous les bits 
	for i in range(0,len(soft_bits)):
		soft_bits[i] = -soft_bits[i]

if constellation == 3:      # 10 -> 11  01 -> 00  11 -> 01  00 -> 10
	for i in range(0,len(soft_bits)-1,2):
		if (soft_bits[i]>0 and soft_bits[i+1]<0) or (soft_bits[i]<0 and soft_bits[i+1]>0):
			soft_bits[i] = soft_bits[i]
			soft_bits[i+1]= -soft_bits[i+1]
		else:
			soft_bits[i] = -soft_bits[i]
			soft_bits[i+1]= soft_bits[i+1]
				
if constellation == 4:      # 01 -> 11  10 -> 00  00 -> 01  11 -> 10	
	for i in range(0,len(soft_bits)-1,2):
		if (soft_bits[i]>0 and soft_bits[i+1]<0) or (soft_bits[i]<0 and soft_bits[i+1]>0):
			soft_bits[i] = -soft_bits[i]
			soft_bits[i+1]= soft_bits[i+1]
		else:
			soft_bits[i] = soft_bits[i]
			soft_bits[i+1]= -soft_bits[i+1]	
	
if constellation == 5:      # 11 -> 11  00 -> 00  10 -> 01  01 -> 10
	for i in range(0,len(soft_bits)-1,2):
		if (soft_bits[i]>0 and soft_bits[i+1]<0) or (soft_bits[i]<0 and soft_bits[i+1]>0):
			soft_bits[i] = -soft_bits[i]
			soft_bits[i+1]= -soft_bits[i+1]
		else:
			soft_bits[i] = soft_bits[i]
			soft_bits[i+1]= soft_bits[i+1]
	
if constellation == 6:      # 00 -> 11  11 -> 00  10 -> 10  01 -> 01
	for i in range(0,len(soft_bits)-1,2):
		if (soft_bits[i]>0 and soft_bits[i+1]<0) or (soft_bits[i]<0 and soft_bits[i+1]>0):
			soft_bits[i] = soft_bits[i]
			soft_bits[i+1]= soft_bits[i+1]
		else:
			soft_bits[i] = -soft_bits[i]
			soft_bits[i+1]= -soft_bits[i+1]
	
if constellation == 7:      # 10 -> 11  01 -> 00  11 -> 10  00 -> 01
	for i in range(0,len(soft_bits)-1,2):
		if (soft_bits[i]>0 and soft_bits[i+1]<0) or (soft_bits[i]<0 and soft_bits[i+1]>0):
			soft_bits[i] = soft_bits[i]
			soft_bits[i+1]= -soft_bits[i+1]
		else:
			soft_bits[i] = soft_bits[i]
			soft_bits[i+1]= -soft_bits[i+1]
			
if constellation == 8:      # 01 -> 11  10 -> 00  11 -> 01  00 -> 10
	for i in range(0,len(soft_bits)-1,2):
		if (soft_bits[i]>0 and soft_bits[i+1]<0) or (soft_bits[i]<0 and soft_bits[i+1]>0):
			soft_bits[i] = -soft_bits[i]
			soft_bits[i+1]= soft_bits[i+1]
		else:
			soft_bits[i] = -soft_bits[i]
			soft_bits[i+1]= soft_bits[i+1]	




g=open("entreeViterbi.bin","wb")
g.write(soft_bits)
g.close()
