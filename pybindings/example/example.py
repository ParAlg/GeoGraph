import gbbs
import geograph
import numpy as np
from utils import *

points = geograph.loadPoints("random.csv")

### example 1 - computing connected component on the 1-nn graph

# 1-nn, no filtering, unweighted
edges = geograph.KnnGraph(points, 1, -1, False)

G = geograph.loadFromEdgeList(edges, True, False)

C = G.Connectivity()

visualizeComponent(points, edges, C, "1nn-cc")

### example 2 - computing MST on the Delaunay graph

# Delanay graph, weighted
edges = geograph.DelaunayGraph(points, True)

E = np.array([np.array([e[0],e[1]]) for e in edges], dtype=np.int32)
visualizeComponent(points, E, np.zeros(points.shape[0],dtype=np.int32), "dt")

G = geograph.loadFromEdgeList(edges, True, True)

T = G.MinimumSpanningForest()
MST = np.array([np.array([e[0],e[1]]) for e in T])
visualizeComponent(points, MST, np.zeros(points.shape[0],dtype=np.int32), "dt-mst")

### example 3 - computing page rank on the 2-skeleton graph

# 2-skeleton, unweighted
edges = geograph.BetaSkeleton(points, 2, False)

G = geograph.loadFromEdgeList(edges, True, False)

R = G.PageRank()

visualizeRank(points, edges, R, "rng-pr")

### example 4 - computing k-core on the 3-nn graph

# 3-nn, weighted, removing >0.3
edges = geograph.KnnGraph(points, 3, 0.3, True)
E = np.array([np.array([e[0],e[1]]) for e in edges], dtype=np.int32)

G = geograph.loadFromEdgeList(edges, True, True)

K = G.KCore()

print(K)

visualizeRank(points, E, K, "3nn-kcore", [str(int(k)) for k in K])
