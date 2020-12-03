
import numpy as np
f = open("sortie2.bin","rb")			#on ouvre le fichier de sortie qui ne contient à priori pas "1acffc1d" ...
bits = np.fromfile(f,dtype = np.uint8)

binary=''
for i in range(len(bits)):				# on convertit les octets en binaire sur 8 bits
	binary+=bin(bits[i])[2:].zfill(8)
	
print(binary.count('00011010110011111111110000011101'))   # on cherche le nbr d'occurence de 
														  # la suite binaire qui correspond à "1acffc1d"
