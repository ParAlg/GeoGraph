### Visualization

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

def visualizeComponent(points, edges, C, name="fig"):
  baseColors = ['tab:blue'
            ,'tab:orange'
            ,'tab:green'
            ,'tab:red'
            ,'tab:purple'
            ,'tab:brown'
            ,'tab:pink'
            ,'tab:gray'
            ,'tab:olive'
            ,'tab:cyan']

  lc = LineCollection(points[edges])
  fig = plt.figure()
  plt.gca().add_collection(lc)
  plt.xlim(points[:,0].min()-.1, points[:,0].max()+.1)
  plt.ylim(points[:,1].min()-.1, points[:,1].max()+.1)
  ax = plt.gca()
  ax.axes.xaxis.set_visible(False)
  ax.axes.yaxis.set_visible(False)
  plt.plot(points[:,0], points[:,1], 'ro', markersize=0)
  for i,p in enumerate(points):
      plt.scatter(p[0], p[1], color=baseColors[C[i] % len(baseColors)], s=200)
  plt.gca().set_aspect('equal', adjustable='box')
  plt.show()
  fig.savefig(name+".pdf")

def visualizeRank(points, edges, R, name="fig", labels=None):
  print(R)
  myMin = min(R)
  myMax = max(R)
  A = [(r-myMin)/(myMax-myMin)+0.1 for r in R]
  A = [min(a,1) for a in A]
  print(A)
  lc = LineCollection(points[edges])
  fig = plt.figure()
  plt.gca().add_collection(lc)
  plt.xlim(points[:,0].min()-.1, points[:,0].max()+.1)
  plt.ylim(points[:,1].min()-.1, points[:,1].max()+.1)
  ax = plt.gca()
  ax.axes.xaxis.set_visible(False)
  ax.axes.yaxis.set_visible(False)
  plt.plot(points[:,0], points[:,1], 'ro', markersize=0)
  for i,p in enumerate(points):
      plt.scatter(p[0], p[1], alpha=A[i], s=200, color='tab:blue')
      if labels:
        plt.annotate(labels[i], (p[0]+0.02, p[1]+0.02), fontsize=20)
  plt.gca().set_aspect('equal', adjustable='box')
  plt.show()
  fig.savefig(name+".pdf")

### Load / generate data

def dataGen(n, save = ""):
  points = np.random.random((n, 2))
  if (save != ""):
    np.savetxt(save, points, delimiter=",")
  return points
