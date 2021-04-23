import numpy as np
import geograph

def loadPoints(fileName):
  return geograph.loadPoints(fileName)

def delaunayGraph(X):
  edges = geograph.DelaunayGraph(X, True)
  return geograph.loadFromEdgeList(edges, True, True)

def knnGraph(X):
  edges = geograph.KnnGraph(X, 3, -1, True)
  print(edges)
  f = open("10k.npy", "wb")
  np.save(f, edges)
  print("saved")
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
  return G.SSSP(0)
