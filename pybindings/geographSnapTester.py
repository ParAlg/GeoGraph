import numpy as np
import geograph

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
