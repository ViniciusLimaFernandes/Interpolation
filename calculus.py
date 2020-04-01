def functionResults():
  values = [15,8,-1]
  return values

def xValues():
  values = [-1,0,3]
  return values

def sumElements(arr):
  result = 0
  numFloat = 4
  for num in arr:
    result += num
  return round(result, numFloat)

def interpolate(x):
  numFloat = 6
  di = []
  xi = xValues()
  fi = functionResults()
  fiDividedBydi = []
  fiDividedBydiTotal = 0
  
  piX = (x-xi[0]) * (x-xi[1]) * (x-xi[2])

  i0 = (x-xi[0]) * (xi[0]-xi[1]) * (xi[0]-xi[2])

  i1 = (xi[1]-xi[0]) * (x-xi[1]) * (xi[1]-xi[2])

  i2 = (xi[2]-xi[0]) * (xi[2]-xi[1]) * (x-xi[2])

  di.append(i0)
  di.append(i1)
  di.append(i2)

  j0 = round((fi[0]/di[0]), numFloat)
  
  j1 = round((fi[1]/di[1]), numFloat)

  j2 = round((fi[2]/di[2]), numFloat)

  fiDividedBydi.append(j0)
  fiDividedBydi.append(j1)
  fiDividedBydi.append(j2)

  fiDividedBydiTotal = sumElements(fiDividedBydi)

  result = piX * fiDividedBydiTotal

  printResult(x, xi, fi, di, fiDividedBydi, piX, fiDividedBydiTotal, result)

  return result 

def printResult(x, xi, fi, di, fiDividedBydi, piX, fiDividedBydiTotal, result):
  print("--------- Lagrange ----------")
  print("Calculating for x =", x)
  print("Xi = ", xi)
  print("Fi = ", fi)
  print("Di = ", di)
  print("Fi/Di = ", fiDividedBydi)
  print("Pi(n+1) = ", piX)
  print("Sum of Fi/Di = ", fiDividedBydiTotal)
  print("Done, result = ", result)