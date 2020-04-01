from calculus import *
from createGraph import plotGraph
  
def validadePoint(x):
  initialNum = -1
  finalNum = 3

  if(x <= initialNum or x >= finalNum):
    print("Point out of range, must be between [", initialNum,",",finalNum,"]")
    exit()
  
def showHome():
  print('-----------------------------------------')
  print('           Lagrange Calculator           ')
  print('                                         ')
  print(' Pick a option:                          ')
  print('         (1) Run Demo With Graph         ')
  print('         (2) Pick a point to calculate   ')
  print('                                         ')
  print('                                         ')
  print('                                         ')
  print('   Developed By: Vinicius Lima Fernandes ')
  print('-----------------------------------------')

def chooseOption():
  option = input()
  option = int(option)

  if(option < 1 or option > 2):
    print("Invalid option!")
    exit()

  return option

def handleOption(option):
  runDemo = 1
  pickPoint = 2
  
  
  if(option == runDemo):
    numFloat = 4
    example = [-0.5,0.5,1.5,2,2.5]
    points = []
    result = 0

    for num in example:
      result = interpolate(num)
      result = round(result, numFloat)
      points.append(result)

    plotGraph(points)
  
  else:
    x = selectPoint()
    validadePoint(x)
    interpolate(x)

def selectPoint():
  point = input("Input a point to calculate with lagrange:\n")
  return float(point)