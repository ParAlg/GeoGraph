#!/usr/bin/env python3
import time

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
    print("  load-time =       {:.5f} sec".format(self.loadTime/1000.0))
    print("  graph-gen-time =  {:.5f} sec".format(self.genTime/1000.0))
    print("  algo-time =       {:.5f} sec".format(self.algTime/1000.0))
    print(" gen+algo-time =    {:.5f} sec".format(self.genTime/1000.0 +\
                                                  self.algTime/1000.0))
    print(" total-time =       {:.5f} sec".format(self.loadTime/1000.0 +\
                                                  self.genTime/1000.0 +\
                                                  self.algTime/1000.0))
