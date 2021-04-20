import gbbs
import geograph
import numpy as np

### Load / generate data

def dataGen(n = 100, save = False):
  points = np.random.random((n, 2))
  if (save):
    np.savetxt("random.csv", points, delimiter=",")
  return points

points = geograph.loadPoints("random.csv")
#points = dataGen(100, False)

### example 1
# compute connected component on a 1-nn graph

knnEdges = geograph.KnnGraph(points, 1)

G = gbbs.loadFromEdgeList(knnEdges, True, False)

C = G.Connectivity()

### example 2
# compute BFS on the relative neighborhood graph

rng = geograph.BetaSkeleton(points, 2)

G = gbbs.loadFromEdgeList(rng, True, False)

weight = G.BFS(0)
