import gbbs
import geograph
import numpy as np
from utils import *

N = 10

points = geograph.loadPoints("data.csv")

### example 1 - computing connected component on filtered knn graph

edges = geograph.KnnGraph(points, 4, 3.2, True)

E = np.array([np.array([e[0],e[1]]) for e in edges], dtype=np.int32)

G = geograph.loadFromEdgeList(edges, True, True)

C = G.Connectivity()

visualizeComponent(points, E, C, "3nn-filter-cc")

### example 2 - computing MST on the Delaunay graph

edges = geograph.DelaunayGraph(points, True)

E = np.array([np.array([e[0],e[1]]) for e in edges], dtype=np.int32)

G = geograph.loadFromEdgeList(edges, True, True)

T = G.MinimumSpanningForest()

MST = np.array([np.array([e[0],e[1]]) for e in T])
visualizeComponent(points, E, np.zeros(points.shape[0],dtype=np.int32), "dt-mst", None, MST)

### example 3 - computing shorest path on Gabriel graph (no visual)

edges = geograph.GabrielGraph(points, True)

G = geograph.loadFromEdgeList(edges, True, True)

SP = G.DeltaStepping(0, 0.01)

### example 4 - computing complete linkage hac on knn graph (no visual)

edges = geograph.KnnGraph(points, 3, -1, True)

G = geograph.loadFromEdgeList(edges, True, True)

CL = G.HierarchicalAgglomerativeClustering("complete", True)

### example A1 - computing page rank on the 2-skeleton graph

edges = geograph.BetaSkeleton(points, 2, False)

G = geograph.loadFromEdgeList(edges, True, False)

R = G.PageRank()

visualizeRank(points, edges, R, "rng-pr")

### example A2 - computing k-core on the 3-nn graph

edges = geograph.KnnGraph(points, 3, 0.3, True)
E = np.array([np.array([e[0],e[1]]) for e in edges], dtype=np.int32)

G = geograph.loadFromEdgeList(edges, True, True)

K = G.KCore()

#visualizeRank(points, E, K, "3nn-kcore", [str(int(k)) for k in K])
