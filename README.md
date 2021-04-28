# GeoGraph

GeoGraph is a framework for shared-memory multicore machines, that supports routines for parallel geometric graph construction and parallel graph processing. GeoGraph contains high performance parallel primitives and algorithms implemented in C++, and includes a Python interface. Currently it generates the following geometric graphs:
* Delaunay graph,
* k-NN graph,
* Gabriel graph,
* beta-skeleton.

GeoGraph can solve a widely of graph problems on these graphs by seamless passing them to highly optimized graph algorithms, including:
* hierarchical agglomerative clustering,
* single-source shortest path,
* minimum spanning tree,
* connected-components,
* breadth-first search,
* page-rank,
* k-core.

# Compilation

Compiler:
* g++ &gt;= 7.4.0 with pthread support

GeoGraph requires two build systems:
* [Bazel](https://docs.bazel.build/versions/master/install.html) 2.1.0
* [CMake](https://cmake.org/install/) 3.10

First, build GeoGraph by executing ``sh compile.sh`` from the project root directory. After that, shared libraries and files will appear in the `pybindings` directory. Then use the Python version listed below and install the Python dependencies:
* Python 3 (tested on Python 3.8)
* Dependencies `pybindings/requirements.txt`

# Example

Navigate to the `pybindings` directory, refer to `example.py` for simple examples of using GeoGraph, and run it by `Python3 example.py`.
