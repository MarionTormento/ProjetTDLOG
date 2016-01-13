def distance_levenshtein(mot1,mot2):
	len1=len(mot1)
	len2=len(mot2)
	d=[0]*((len1+1)*(len2+1))
	for i in range(len1+1):
		d[(len2+1)*i]=i
	for j in range(len2+1):
		d[j]=j
	for i in range(1,len1+1):
		for j in range(1,len2+1):
			if mot1[i-1]==mot2[j-1]:
				cout=0
			else:
				cout=1
			d[(len2+1)*i+j]=min((d[(len2+1)*(i-1)+j]+1), (d[(len2+1)*i+j-1]+1), (d[(len2+1)*(i-1)+j-1]+cout))
	print(d[(len2+1)*len1+len2])



distance_levenshtein("arbres","arbres")
distance_levenshtein("arbres","arbros")
distance_levenshtein("arbres","maison")





