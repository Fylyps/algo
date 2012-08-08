import sys

from network.Network import Network

def findShortestExtendingPath(net, level = None, visited = None):
	if not level: level = {0: (sys.maxint, [0])}
	if not visited: visited = [0]

	if level.has_key(net.n - 1):
		return level[net.n - 1] 

	nextlevel = {}

	for v in level.keys():
		oldc, oldpath = level[v]
		for w in xrange(net.n):
			if w not in visited and net.c[v][w]:
				nextlevel[w] = (min(oldc, net.c[v][w]), oldpath + [w])
				visited.append(w)

	if not nextlevel.keys():
		return 0, [] 
	return findShortestExtendingPath(net, nextlevel, visited)


def edmondsKarp(net):
	flow = Network(net.n)
	residual = net.substract(flow)
	minc, path = findShortestExtendingPath(residual)
	while minc:
		flow.append(minc, path)
		residual = net.substract(flow)
		minc, path = findShortestExtendingPath(residual)
	return flow

net = Network()
net.read()

print edmondsKarp(net).sumFlow(0)
