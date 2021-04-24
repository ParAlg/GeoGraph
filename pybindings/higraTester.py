import numpy as np
import higra as hg

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
