#!/usr/bin/env python3
import numpy as np
import geograph
import geographTest as gt
from benchmark import Benchmark

def delaunayGraph(X):
  edges = geograph.DelaunayGraph(X, True)
  geograph.saveEdgeSnap("tmp.snap", edges)
  return geograph.loadFromSnap("tmp.snap", True, True)

def knnGraph(X):
  edges = geograph.KnnGraph(X, 3, -1, True)
  geograph.saveEdgeSnap("tmp.snap", edges)
  return geograph.loadFromSnap("tmp.snap", True, True)

def filteredKnnGraph(X):
  edges = geograph.KnnGraph(X, 3, 3.0, True)
  geograph.saveEdgeSnap("tmp.snap", edges)
  return geograph.loadFromSnap("tmp.snap", True, True)

def gabrielGraph(X):
  edges = geograph.GabrielGraph(X, True)
  geograph.saveEdgeSnap("tmp.snap", edges)
  return geograph.loadFromSnap("tmp.snap", True, True)

def cleanUp():
  import os
  os.remove("tmp.snap")

if __name__ == "__main__":
  import sys
  filePath = sys.argv[1]

  gg1 = Benchmark("geograph-dt-mst", gt.loadPoints, delaunayGraph, gt.MST)
  gg1.run(filePath)

  gg2 = Benchmark("geograph-3nn-clink", gt.loadPoints, knnGraph, gt.CLINK)
  gg2.run(filePath)

  gg3 = Benchmark("geograph-3nn-filtered-cc", gt.loadPoints, filteredKnnGraph, gt.CC)
  gg3.run(filePath)

  gg4 = Benchmark("geograph-gabriel-sssp", gt.loadPoints, gabrielGraph, gt.SSSP)
  gg4.run(filePath)

  gg1.info()
  gg2.info()
  gg3.info()
  gg4.info()

  cleanUp()
