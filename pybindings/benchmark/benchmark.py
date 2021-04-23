import time
import higraTester as ht
import geographTester as gt

'''
Benchmark = data set + target impl

1) Data load time
2) Graph gen time
4) Graph alg time
'''

class Benchmark:
  filePath = None
  loadTime = 0
  genTime = 0
  algTime = 0
  t = -1

  def __init__(self, _name, _loader, _graphGen, _runAlgo):
    self.name = _name
    self.loader = _loader
    self.graphGen = _graphGen
    self.runAlgo = _runAlgo

  def milliTime(self):
    tp = self.t
    self.t = round(time.time() * 1000)
    return self.t - tp

  def run(self, _filePath):
    self.filePath = _filePath
    self.milliTime()
    X = self.loader(self.filePath)
    self.loadTime = self.milliTime()
    G = self.graphGen(X)
    self.genTime = self.milliTime()
    R = self.runAlgo(G)
    self.algTime = self.milliTime()

  def info(self):
    print("\n---", self.name, "--- data set", self.filePath)
    print("  load-time =       {:.3f} sec".format(self.loadTime/1000.0))
    print("  graph-gen-time =  {:.3f} sec".format(self.genTime/1000.0))
    print("  algo-time =       {:.3f} sec".format(self.algTime/1000.0))
    print(" total-time =       {:.3f} sec".format(self.loadTime/1000.0 +\
                                       self.genTime/1000.0 +\
                                       self.algTime/1000.0))

def bench(filePath):

  hg1 = Benchmark("higra-dt-mst", ht.loadPoints, ht.delaunayGraph, ht.MST)
  hg1.run(filePath)

  hg2 = Benchmark("higra-3nn-clink", ht.loadPoints, ht.knnGraph, ht.CLINK)
  hg2.run(filePath)

  gg1 = Benchmark("geograph-dt-mst", gt.loadPoints, gt.delaunayGraph, gt.MST)
  gg1.run(filePath)

  gg2 = Benchmark("geograph-3nn-clink", gt.loadPoints, gt.knnGraph, gt.CLINK) # todo clink
  gg2.run(filePath)

  gg3 = Benchmark("geograph-3nn-filtered-cc", gt.loadPoints, gt.filteredKnnGraph, gt.CC)
  gg3.run(filePath)

  gg4 = Benchmark("geograph-gabriel-sssp", gt.loadPoints, gt.gabrielGraph, gt.SSSP)
  gg4.run(filePath)

  hg1.info()
  hg2.info()

  gg1.info()
  gg2.info()
  gg3.info()
  gg4.info()
