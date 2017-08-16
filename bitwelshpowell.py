import numpy as np

# ubah file data inputan ke matriks insidensi
def data2inc(namafile, n_baris, n_kolom):
	data1dimensi = open(namafile).read().splitlines()
	data1dimensi = [ int(i) for i in data1dimensi ]
	inc = np.array(data1dimensi).reshape((n_baris, n_kolom))
	return inc

# ubah insidensi mahasiswa --> makul ke adjacency makul
def inc2adj(inc_mhs_makul):
	n_makul = inc_mhs_makul.shape[1]

	adj = np.zeros((n_makul,n_makul), dtype=np.uint8)

	for baris in inc_mhs_makul:
		titik_hidup = [ i for i in range(n_makul) if baris[i] == 1 ]
		banyaknya_hidup = len(titik_hidup)
		if banyaknya_hidup > 1:
			for i in range(banyaknya_hidup - 1):
				for j in range(i+1, banyaknya_hidup):
					adj[titik_hidup[i], titik_hidup[j]] = 1
					adj[titik_hidup[j], titik_hidup[i]] = 1
	return adj

# coba dulu
insidenku = data2inc('kode incidency.txt', 16, 9)
print insidenku

adjacencyku = inc2adj(insidenku)
print adjacencyku

# tambahkan derajat di baris dan kolom baru
# buat matriks baru yang ukurannya menjadi lebih besar 1 baris dan 1 kolom
def adj_tambahan(adjacencyMat):
	v = adjacencyMat.shape[1]
	adj_der = np.zeros((v+1, v+1), dtype=np.uint8)
	adj_der[:v,:v] = adjacencyMat
	print adj_der

	jml = adjacencyMat.sum(axis=1)

	adj_der[:v,v] = jml
	adj_der[v,:v] = jml

	adj_tanda = np.zeros((v+2, v+2), dtype=np.uint8)
	adj_tanda[:v+1,:v+1] = adj_der

	adj_tanda[:v,v+1] = np.arange(v)
	adj_tanda[v+1,:v] = np.arange(v)
	return adj_tanda

a = adj_tambahan(adjacencyku)

def adj_urut(adj_tanda):
	v = adj_tanda.shape[1] - 2
	urut = adj_tanda[:v,v].argsort()[::-1]
	# copy adj_tanda
	adj_sort = adj_tanda
	adj_sort[:v,:v+2] = adj_tanda[urut]
	#~ print adj_sort
	adj_sort[:v+2,:v] = adj_tanda[:,urut]
	return adj_sort

aUrut = adj_urut(a)
print 'a urut:\n',aUrut