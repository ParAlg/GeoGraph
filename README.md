# GeoGraph

GeoGraph is a framework for shared-memory multicore machines, that supports routines for parallel geometric graph construction and parallel graph processing. GeoGraph contains high performance parallel primitives and algorithms implemented in C++, and includes a Python interface.

**Geometric graph generators**

* Delaunay Graph
* K-NN Graph
* Gabriel Graph
* Beta Skeleton

**Graph algorithms**

* Hierarchical Agglomerative Clustering
* Single Source Shortest Path
* Minimum Spanning Tree
* Connected Components
* Breadth-First Search
* Page Rank
* K-Core

# Compilation

Compiler:
* g++ &gt;= 7.4.0 with pthread support

GeoGraph requires two build systems:
* [Bazel](https://docs.bazel.build/versions/master/install.html) >=2.1.0
* [CMake](https://cmake.org/install/) >=3.10

First, build GeoGraph by ``sh compile.sh`` from the project root directory, after which shared libraries and files will appear in the `pybindings` directory. Install the Python dependencies in `pybindings/requirements.txt` using Python 3.

# Example

Here is an example of generating the 1-NN graph of ``pybindings/data.csv``, and running the minimum-spanning tree algorithm:

```python
import geograph

points = geograph.loadPoints("data.csv")

edges = geograph.KnnGraph(points, k = 1, weighted = True)

G = geograph.loadFromEdgeList(edges, symmetric = True, weighted = True)

F = G.MinimumSpanningForest()
```

Please refer to `pybindings/example.py` for more examples.
