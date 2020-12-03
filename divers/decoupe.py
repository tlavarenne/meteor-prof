
import numpy as np

f=open("meteor.s","rb")
byte = np.fromfile(f, dtype=np.int8)
f.close()
g=open("binarymeteor3.s","wb")
g.write(byte[len(byte)//2:len(byte)//2+50*16384])
g.close()
