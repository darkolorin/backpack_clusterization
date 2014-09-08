__author__ = 'olorin'
import numpy
import time


#Get execution time of a function
def gettime(fun, *args):
    start = time.time()
    fun(*args)
    end = time.time()
    return str(end - start)


#cluster method provides simple interface to k-means clusterization with limited weight of a cluster
#coordinates - array of (x,y) coordinates of a point: 2-dim array
#hours - weight of each point, for user it's time to spent at this location (museum, park etc): array
#days - number of clusters, for user it's a trip  duration in days: integer
#return array of points for each day of a trip
def cluster(coordinates, hours, days):
    transitTime = 3  # approximation of transit time between points
    maxW = hours - transitTime  # maximym weight of a cluster defined by hours in each of a trip minus summ of transit times
    points = coordinates
    k = days
    #init clusters randomly
    centroids = numpy.random.random_sample((days, 2))

    return 0

#Generation parameters
number_of_points = 5

#create dataset of points in format [(x,y),...]
mydata = numpy.random.random_sample((number_of_points, 2))
print(mydata)

#generate time to spent for each point
myhours = numpy.random.random_integers(3, size=(number_of_points, 1.))
print(myhours)

#generate days for trip
mydays = numpy.random.random_integers(0, 7)
print(mydays)

cluster(mydata,myhours,mydays)