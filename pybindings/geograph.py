import gbbs
import pypargeo

'''
IO functions
'''

def loadPoints(fileName):
  return pypargeo.loadPoints(fileName)

def loadGraph(graphPath="",undirected=True, compressed=False, binary=False):
  return gbbs.loadGraph(graphPath,undirected, compressed, binary)

'''
Edge generators
'''

def KnnGraph(points, k):
  return pypargeo.KnnGraph(points, k)

def DelaunayGraph(points):
  return pypargeo.delaunayGraph(points)

def GabrielGraph(points):
  return pypargeo.GabrielGraph(points)

def BetaSkeleton(points, beta):
  return pypargeo.BetaSkeleton(points, beta)

'''
Graph constructors
'''

def loadFromEdgeList(edges):
  return gbbs.loadFromEdgeList(edges)
