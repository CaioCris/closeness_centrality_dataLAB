# -*- coding: utf-8 -*-

import pandas as pd
from numpy import argsort, asarray, empty, NAN

#Vendo qual a distancia entre cada um dos nodes
def closeness_centrality(pairs, root):
	
	visited = [False] * 100
	visited[root] = True
	
	distance = empty(100)
	distance[:] = NAN
	
	distance[root] = 0
	
	current_distance = 0
	
	while True:

		if all(visited):
			break

		for node in range(100):
			
			if distance[node] == current_distance:
				
				for pair in pairs:
					
					if pair[0] == node and not visited[pair[1]]:
						visited[pair[1]] = True
						distance[pair[1]] = current_distance + 1
						
					if pair[1] == node and not visited[pair[0]]:
						visited[pair[0]] = True
						distance[pair[0]] = current_distance + 1
	
		current_distance += 1
	
	return float(99) / sum(distance)

#Abrir o arquivo com a lista, e organizando a lista de nodes
def file_data():
	
	with open('data/edges.dat') as f:
		lines = f.readlines()

	pairs = [i.split() for i in lines]

	for i in range(len(pairs)):
		pairs[i][0] = int(pairs[i][0])
		pairs[i][1] = int(pairs[i][1])

	return pairs

#Moldando a forma como deve sair os dados, forma visual
def print_results(closeness):

	position = argsort(closeness)[::-1]
	
	distance_closeness = closeness[position]

	data_array = asarray([position, distance_closeness])

	df = pd.DataFrame(data=data_array.T, columns = ['Node','Closeness'])

	df['Node'] = df['Node'].map(lambda x: int(x))
	df.index.name = 'Posição'
	pd.set_option('display.max_rows', 100)

	print(df)

#Chamando as funçoões
if __name__ == "__main__":

	Nodes = file_data()
	
	closeness = asarray([closeness_centrality(Nodes, i) for i in range(100)])

	print_results(closeness)