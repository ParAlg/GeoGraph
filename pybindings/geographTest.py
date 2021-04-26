#!/usr/bin/env python3
import numpy as np
import geograph
from benchmark import Benchmark

def loadPoints(fileName):
  return geograph.loadPoints(fileName)

def delaunayGraph(X):
  edges = geograph.DelaunayGraph(X, True)
  return geograph.loadFromEdgeList(edges, True, True)

def knnGraph(X):
  edges = geograph.KnnGraph(X, 3, -1, True)
  return geograph.loadFromEdgeList(edges, True, True)

def filteredKnnGraph(X):
  edges = geograph.KnnGraph(X, 3, 3.0, True)
  return geograph.loadFromEdgeList(edges, True, True)

def gabrielGraph(X):
  edges = geograph.GabrielGraph(X, True)
  return geograph.loadFromEdgeList(edges, True, True)

def MST(G):
  return G.MinimumSpanningForest()

def SLINK(G):
  return G.HierarchicalAgglomerativeClustering("single", True)

def CLINK(G):
  return G.HierarchicalAgglomerativeClustering("complete", True)

def CC(G):
  return G.Connectivity()

def SSSP(G):
  return G.DeltaStepping(0, 0.01)

if __name__ == "__main__":
  import sys
  filePath = "data.csv"
  if len(sys.argv) > 1:
    filePath = sys.argv[1]

  gg1 = Benchmark("geograph-dt-mst", loadPoints, delaunayGraph, MST)
  gg1.run(filePath)

  gg2 = Benchmark("geograph-3nn-clink", loadPoints, knnGraph, CLINK)
  gg2.run(filePath)

  gg3 = Benchmark("geograph-3nn-filtered-cc", loadPoints, filteredKnnGraph, CC)
  gg3.run(filePath)

  gg4 = Benchmark("geograph-gabriel-sssp", loadPoints, gabrielGraph, SSSP)
  gg4.run(filePath)

  gg1.info()
  gg2.info()
  gg3.info()
  gg4.info()
