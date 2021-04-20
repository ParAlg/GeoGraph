### Visualization

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

def visualizeComponent(points, edges, C):
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
  #fig.savefig(name+".png")

def visualizeRank(points, edges, R):
  A = [(r-min(R))/(max(R)-min(R)) for r in R]
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
  plt.gca().set_aspect('equal', adjustable='box')
  plt.show()
  #fig.savefig(name+".png")

### Load / generate data

def dataGen(n, save = ""):
  points = np.random.random((n, 2))
  if (save != ""):
    np.savetxt(save, points, delimiter=",")
  return points
