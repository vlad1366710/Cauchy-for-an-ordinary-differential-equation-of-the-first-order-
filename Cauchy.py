import numpy
def func(x,y):
   return((y*y-x*x)/2*x*y)

def koshi(x,y):
    h=0.1
    h2=0.05
    n1=int(1/h+1)
    n2=int(1/h2+1)
    xi1 = numpy.zeros((n1)) 
    yi1 = numpy.zeros((n1)) 
    
    xi1[0] = x
    yi1[0] = y
    for i in range(1,n1):
        xi1[i] = xi1[i - 1] + h
        yi1[i] = yi1[i - 1] + h * func(xi1[i - 1], yi1[i - 1])
    
    xi2 = numpy.zeros((n2)) 
    yi2 = numpy.zeros((n2)) 
    xi2[0] = x
    yi2[0] = y
    for i in range(1,n2):
        xi2[i] = xi2[i - 1] + h2
        yi2[i] = yi2[i - 1] + h2 * func(xi2[i - 1], yi2[i - 1])
  
    for i in range(n1):
        i2=i*2
        resul = yi2[i2] + (yi2[i2]-yi1[i]) / (2*2-1)
        print ('x', round(xi1[i],3),"=", resul)

koshi(1,0.5)

