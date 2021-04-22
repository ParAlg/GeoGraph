import pypargeo
import gbbs

'''
IO functions
'''

def loadPoints(fileName):
  return pypargeo.loadPoints(fileName)

def loadGraph(graphPath="",undirected=True, compressed=False, binary=False):
  return gbbs.loadGraph(graphPath, undirected, compressed, binary)

def loadFromEdgeList(edges, symmetric=True, weighted=False):
  return gbbs.loadFromEdgeList(edges, symmetric, weighted)

'''
Edge generators
'''

def KnnGraph(points, k, eps=-1, weighted=False):
  if eps > 0:
    weighted = True
  if weighted:
    return pypargeo.WghKnnGraph(points, k, eps)
  else:
    return pypargeo.KnnGraph(points, k)

def DelaunayGraph(points, weighted=False):
  if weighted:
    return pypargeo.WghDelaunayGraph(points)
  else:
    return pypargeo.DelaunayGraph(points)

def GabrielGraph(points, weighted=False):
  if weighted:
    return pypargeo.WghGabrielGraph(points)
  else:
    return pypargeo.GabrielGraph(points)

def BetaSkeleton(points, beta, weighted=False):
  if weighted:
    return pypargeo.WghBetaSkeleton(points, beta)
  else:
    return pypargeo.BetaSkeleton(points, beta)
