import sys

from network.Network import Network

def findBlockingFlow(net):
	blocking = Network(net.n)	# start with empty flow
	v = 0						# start from source
	path = [0]
	stepable = any([net.c[v][w] for w in xrange(net.n)])

	while v != 0 or stepable:
		if stepable:
			# advance
			w = 0
			while not net.c[v][w]:
				w += 1
			path.append(w)
			v = w

			if w == net.n - 1:
				# augment
				path_edges = zip(path[:-1], path[1:])
				minc = sys.maxint
				for v, w in path_edges:
					minc = min(minc, net.c[v][w])
				
				for v, w in path_edges:
					blocking.c[v][w] += minc
					blocking.c[w][v] = -blocking.c[v][w]
					net.c[v][w] -= minc

				v = 0 # look for the new path
				path = [0]
		else:
			# retreat
			w = path.pop()
			v = path[-1]
			net.c[v][w] = 0
		
		stepable = any([net.c[v][w] for w in xrange(net.n)])

	return blocking

def getLayerNet(net):
	layers = Network(net.n)
	current = [0]
	visited = current
	nextLayer = []
	while current and net.n - 1 not in visited:
		for v in current:
			for w in xrange(net.n):
				if net.c[v][w] and w not in visited:
					nextLayer.append(w)
					layers.setFlow(v, w, net.c[v][w])
		current = nextLayer
		visited = visited + nextLayer
		nextLayer = []
	return net.n -1 in visited, layers

def dinic(net):
	flow = Network(net.n)
	residual = net.substract(flow)
	extended, layerNet = getLayerNet(residual)
	while extended:
	 	blocking = findBlockingFlow(layerNet)
		flow.appendFlow(blocking)
		residual = net.substract(flow)
		extended, layerNet = getLayerNet(residual)
	return flow

'''
net = Network()
net.read(sys.stdin)
print dinic(net).sumFlow(0)
'''
