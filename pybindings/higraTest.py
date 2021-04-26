#!/usr/bin/env python3
import numpy as np
import higra as hg
from benchmark import Benchmark

def loadPoints(fileName):
  return np.loadtxt(fileName, delimiter=",")

def delaunayGraph(X):
  graph, edge_weights = hg.make_graph_from_points(X, 'delaunay')
  return tuple((graph, edge_weights))

def knnGraph(X):
  graph, edge_weights = hg.make_graph_from_points(X, 'knn', n_neighbor=3)
  return tuple((graph, edge_weights))

def MST(G):
  return hg.minimum_spanning_tree(G[0], G[1])

def SLINK(G):
  return hg.binary_partition_tree_single_linkage(G[0], G[1])

def CLINK(G):
  return hg.binary_partition_tree_complete_linkage(G[0], G[1])

if __name__ == "__main__":
  import sys
  filePath = "data.csv"
  if len(sys.argv) > 1:
    filePath = sys.argv[1]

  hg1 = Benchmark("higra-dt-mst", loadPoints, delaunayGraph, MST)
  hg1.run(filePath)

  hg2 = Benchmark("higra-3nn-clink", loadPoints, knnGraph, CLINK)
  hg2.run(filePath)

  hg1.info()
  hg2.info()
