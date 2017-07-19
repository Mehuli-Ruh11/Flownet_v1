#! /usr/bin/python
# Author: Ruoteng Li
# Date: 6th Aug 2016
"""
Demo.py
This file demonstrates how to use kittitool module to read
 and visualize flow file saved in kitti format .png
"""
from lib import flowlib as fl

for i in range(4999,5000):
	# read Middlebury format optical flow file (.flo)
	print "Visualizing Middlebury flow example ..."
	flow_file_Middlebury = ('./data/ChairsSDHom/data/train1/flow/00003.flo')
	flow_Middlebury = fl.read_flow(flow_file_Middlebury)
	fl.visualize_flow(flow_Middlebury)

	print "Visualizing Middlebury flow example ..."
	flow_file_Middlebury1 = ('flownetc-pred-000%d.flo'%i)
	flow_Middlebury1 = fl.read_flow(flow_file_Middlebury1)
	fl.visualize_flow(flow_Middlebury1)


