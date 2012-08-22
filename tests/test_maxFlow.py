# -*- coding: utf-8 -*-	
'''
File: test_maxFlow.py
Author: Filip Stachura
Description: tests for max flow algorithms
'''

import sys, os
from cStringIO import StringIO
pjoin = os.path.sep.join
libpath = pjoin([os.path.dirname(__file__),'..'])
sys.path.append(libpath) 

import maxFlow
from maxFlow.fordFulkerson import FordFulkerson
from maxFlow.edmondsKarp import EdmondsKarp
from maxFlow.dinic import Dinic 
from maxFlow.network.Network import Network

def run_single(algorithm, test_id):
	test_path = pjoin(['tests','maxFlow','basic'])
	in_file = file(pjoin([test_path,'in', test_id + '.in']))
	output = file(pjoin([test_path,'out', test_id + '.out'])).read().strip()

	net = Network()
	net.read(in_file)
	returned = str(algorithm(net).sumFlow(0)).strip()

	info = "Algorithm returned:\n%s\n\nCorrect output is:\n%s\n"
	assert output == returned, info % (returned, output)


class TestFordFulkerson:

	def test_1(self): run_single(FordFulkerson.fordFulkerson, "1")
	def test_2(self): run_single(FordFulkerson.fordFulkerson, "2")
	def test_3(self): run_single(FordFulkerson.fordFulkerson, "3")
	def test_4(self): run_single(FordFulkerson.fordFulkerson, "4")


class TestEdmondsKarp:

	def test_1(self): run_single(EdmondsKarp.edmondsKarp, "1")
	def test_2(self): run_single(EdmondsKarp.edmondsKarp, "2")
	def test_3(self): run_single(EdmondsKarp.edmondsKarp, "3")
	def test_4(self): run_single(EdmondsKarp.edmondsKarp, "4")


class TestDinic:

	def test_1(self): run_single(Dinic.dinic, "1")
	def test_2(self): run_single(Dinic.dinic, "2")
	def test_3(self): run_single(Dinic.dinic, "3")
	def test_4(self): run_single(Dinic.dinic, "4")


