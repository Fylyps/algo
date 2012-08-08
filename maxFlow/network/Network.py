from common.scanf import scanf

class Network():

	def __init__(self, n = 0):
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

	def sumFlow(self, v):
		return sum(self.c[v])

	def read(self):
		n, m = scanf("%d %d")
		self.__init__(n)	
		for i in xrange(m):
			a, b, c = scanf("%d %d %d")
			self.setFlow(a, b, c)

