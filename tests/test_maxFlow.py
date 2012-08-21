# -*- coding: utf-8 -*-	
'''
File: test_maxFlow.py
Author: Filip Stachura
Description: tests for max flow algorithms
'''

import sys, os
from cStringIO import StringIO
pjoin = os.path.sep.join
libpath = pjoin(['.','..'])
sys.path.append(libpath) 
import maxFlow
from maxFlow.fordFulkerson import FordFulkerson


s = StringIO.StringIO('Hello, world!')
sys.stdin = s ; r = raw_input('What you say?\n') ; sys.stdin = sys.__stdin__ 


class TestFordFulkerson:
    def test_1(self):
		test_path = pjoin(['maxFlow','basic'])
		in_path = pjoin([test_path,'in','1.in'])
		out_path = pjoin([test_path,'out','1.out'])

		sys.stdin = file(in_path)
		sys.stdout = test_stdout = StringIO()
	
		net = Network()
		net.read()
		print FordFulkerson.fordFulkerson(net).sumFlow(0)

		returned = test_stdout.getvalue()
		sys.stdout = sys.__stdout__ 

		correct = file(out_path).read()
		print correct
		print returned
