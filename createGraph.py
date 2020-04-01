import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def plotGraph(pointsArray):
  print("\nCreating graph...")
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)

  points = pointsArray
  print("Points = ", points)

  ax.plot(points)
  fig.savefig('./graphs/graph.png')
  print("Your graph are done! File: graphs/graph.png")