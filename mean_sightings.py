#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.mlab as ml
def get_sightings(filename,focusbiosig):
	tab = ml.csv2rec(filename) 
	focusbiosig = focusbiosig.capitalize()
	totalrecs = 0.0
	totalcount = 0.0
	for rec in tab:
		if rec['biosignature'] == focusbiosig:
			totalrecs = totalrecs + 1 
			totalcount = totalcount + rec['count']
	if totalrecs == 0:
		mean_sigs = 0
	else:
		mean_sigs = totalcount/totalrecs
	return totalrecs, mean_sigs
if __name__ == '__main__':
	print sys.argv[1]
	print sys.argv[2]
	filename = sys.argv[1]
	focusbiosig = sys.argv[2]
	print get_sightings(filename,focusbiosig)

