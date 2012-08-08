from common.scanf import scanf
import sys

class Network():

	def __init__(self, n):
		self.n = n
		self.c = [[0 for i in xrange(n)] for i in xrange(n)] 

	def setFlow(self, f, t, v):
		self.c[f][t] = v

	def __str__(self):
		output = "Network of %d vertexes" % self.n
		for a in xrange(self.n):
			for b in xrange(self.n):
				if self.c[a][b]:
					output += "\n[%d] -> %d -> [%d]" % (a, self.c[a][b], b)
		return output

	def append(self, minc, path):
		for i in xrange(len(path)-1):
			v = path[i]
			w = path[i+1]
			self.c[v][w] += minc
			self.c[w][v] -= minc

	def substract(self, flow):
		residual = Network(self.n)
		for a in xrange(self.n):
			for b in xrange(self.n):
				residual.setFlow(a, b, max(0, self.c[a][b] - flow.c[a][b]))
		return residual

def readNetwork():
	n, m = scanf("%d %d")
	net = Network(n)
	for i in xrange(m):
		a, b, c = scanf("%d %d %d")
		net.setFlow(a, b, c)
	return net

def findExtendingPath(net, v=0, path=[0], minc=sys.maxint):
	if v == net.n -1:
		return minc, path

	for w in xrange(net.n):
		if net.c[v][w] and w not in path:
			outc, outpath = findExtendingPath(net, w, path + [w], min(minc, net.c[v][w]))
			if outc: return outc, outpath

	return False, False 
	

def fordFulkerson(net):
	print net
	flow = Network(net.n)
	residual = net.substract(flow)
	minc, path = findExtendingPath(residual)
	while minc:
		#print "extending path found"
		#print minc, path
		flow.append(minc, path)
		residual = net.substract(flow)
		#print residual
		minc, path = findExtendingPath(residual)
	return flow

print fordFulkerson(readNetwork())
