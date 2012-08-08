import sys

from network.Network import Network


def findExtendingPath(net, v = 0, path = [0], minc = sys.maxint):
	if v == net.n -1:
		return minc, path

	for w in xrange(net.n):
		if net.c[v][w] and w not in path:
			outc, outpath = findExtendingPath(net, w, path + [w], min(minc, net.c[v][w]))
			if outc: return outc, outpath

	return False, False 

def fordFulkerson(net):
	flow = Network(net.n)
	residual = net.substract(flow)
	minc, path = findExtendingPath(residual)
	while minc:
		flow.append(minc, path)
		residual = net.substract(flow)
		minc, path = findExtendingPath(residual)
	return flow


net = Network()
net.read()
print fordFulkerson(net).sumFlow(0)

