#~ def sks2Adj(NamaFile_sks, n_makul):
	#~ sks = open(NamaFile_sks).read().splitlines()
	#~ duasks = [i for i in range(n_makul) if sks[i] == 2]
import numpy as np

NamaFile_sks = "sks.txt"
n_makul = 118

sks = open(NamaFile_sks).read().splitlines()
sks = np.array([ int(i) for i in sks ])
duasks = np.array([i for i in range(n_makul) if sks[i] == 2])
tigasks = np.array([i for i in range(n_makul) if sks[i] == 3])
n_duasks = len(duasks)
n_tigasks = len(tigasks)

if n_duasks >1:
	for i in range(n_duasks):
		for j in range(n_tigasks):
			adj

print sks
print duasks
print hku