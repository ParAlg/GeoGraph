### Visualization

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

def visualizeComponent(points, edges, C, name="fig", labels=None, edges2=None):
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

  fig = plt.figure()
  lc = LineCollection(points[edges])
  plt.gca().add_collection(lc)
  if edges2 is not None:
    lc2 = LineCollection(points[edges2], lw=4, color='r')
    plt.gca().add_collection(lc2)
  myMin = min(points[:,0].min(), points[:,1].min())
  myMax = max(points[:,0].max(), points[:,1].max())
  plt.xlim(myMin-1, myMax+1)
  plt.ylim(myMin-1, myMax+1)
  ax = plt.gca()
  ax.axes.xaxis.set_visible(True)
  ax.axes.yaxis.set_visible(True)
  plt.plot(points[:,0], points[:,1], 'ro', markersize=0)
  for i,p in enumerate(points):
      plt.scatter(p[0], p[1], color=baseColors[C[i] % len(baseColors)], s=80)
      if labels:
        plt.annotate(labels[i], (p[0]+0.2, p[1]+0.2), fontsize=20)
  plt.gca().set_aspect('equal', adjustable='box')
  plt.show()
  fig.savefig(name+".pdf")

def visualizeRank(points, edges, R, name="fig", labels=None):
  myMin = min(R)
  myMax = max(R)
  A = [(r-myMin)/(myMax-myMin)+0.1 for r in R]
  A = [min(a,1) for a in A]

  lc = LineCollection(points[edges])
  fig = plt.figure()
  plt.gca().add_collection(lc)
  plt.xlim(points[:,0].min()-1, points[:,0].max()+1)
  plt.ylim(points[:,1].min()-1, points[:,1].max()+1)
  ax = plt.gca()
  ax.axes.xaxis.set_visible(True)
  ax.axes.yaxis.set_visible(True)
  plt.plot(points[:,0], points[:,1], 'ro', markersize=0)
  for i,p in enumerate(points):
      plt.scatter(p[0], p[1], alpha=A[i], s=80, color='tab:blue')
      if labels:
        plt.annotate(labels[i], (p[0]+0.2, p[1]+0.2), fontsize=20)
  plt.gca().set_aspect('equal', adjustable='box')
  plt.show()
  fig.savefig(name+".pdf")

### Load / generate data

def uniformDataGen(n, save = ""):
  points = np.random.random((n, 2))
  points = points * 10
  if (save != ""):
    np.savetxt(save, points, delimiter=",")
  return points

def clusteredDataGen(n, save = ""):
  import sklearn.datasets
  points, labels = sklearn.datasets.make_blobs(n, cluster_std=[1.0, 2.5, 0.5], random_state=220)
  if (save != ""):
    np.savetxt(save, points, delimiter=",")
  return points

def dataStore(points, save):
  np.savetxt(save, points, delimiter=",")
