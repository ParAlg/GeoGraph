import gbbs
import geograph
import numpy as np
from utils import *

points = geograph.loadPoints("random.csv")

### example 1 - computing connected component on the 1-nn graph

edges = geograph.KnnGraph(points, 1)

G = gbbs.loadFromEdgeList(edges, True, False)

C = G.Connectivity()

visualizeComponent(points, edges, C)

### example 2 - computing page rank on the 2-skeleton graph

edges = geograph.BetaSkeleton(points, 2)

G = gbbs.loadFromEdgeList(edges, True, False)

R = G.PageRank()

visualizeRank(points, edges, R)
