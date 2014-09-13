__author__ = 'olorin'
import numpy
import time
import matplotlib.pyplot as plt


#Get execution time of a function
def get_time(fun, *args):
    start = time.time()
    fun(*args)
    end = time.time()
    return str(end - start)


#Get cluster labels for each point
def get_eulcidean(x, y, x1, y1):
    distance = numpy.sqrt(numpy.power((x - x1), 2) + numpy.power((y-y1), 2))
    return distance


def get_labels(x_p, y_p, x_c, y_c):
    c_k = numpy.array([])
    for i in range(len(x_p)-1):
        dist = numpy.array([])
        for j in range(len(x_c)-1):
            dist = numpy.append(dist, [get_eulcidean(x_p[i], y_p[i], x_c[j], y_c[j])])
        print(dist)
        c_k = numpy.append(c_k, [numpy.argmin(dist)])
    return c_k


def get_centroids(x_p, y_p, c_k, k):
    return 0


#Cluster method provides simple interface to k-means clusterization with limited weight of a cluster
#coordinates - array of (x,y) coordinates of a point: 2-dim array
#hours - weight of each point, for user it's time to spent at this location (museum, park etc): array
#days - number of clusters, for user it's a trip  duration in days: integer
#return array of points for each day of a trip
def cluster(coordinates, hours, days, hours_in_day):
    transitTime = 3  # approximation of transit time between points
    #TO_DO get time for transit by calculating distance between points and average speed
    maxW = hours_in_day - transitTime  # maximum weight of a cluster defined by hours in each of a trip minus sum of transit times
    points = coordinates
    x_points = [p[0] for p in coordinates]
    y_points = [p[1] for p in coordinates]
    w_points = [p[0] for p in hours]
    k = days
    #init clusters randomly
    centroids = numpy.random.random_sample((days, 2))
    x_c = [p[0] for p in centroids]
    y_c = [p[1] for p in centroids]
    print(get_labels(x_points, y_points, x_c, y_c))
    #draw points
    #plt.scatter(x_points, y_points)
    #plt.scatter(x_c, y_c, marker=u's', c=u'r', s=40)
    #plt.show()

    return 0

#Generation parameters
number_of_points = 10

#create dataset of points in format [(x,y),...]
mydata = numpy.random.random_sample((number_of_points, 2))
#print(mydata)

#generate time to spent for each point
myhours = numpy.random.random_integers(3, size=(number_of_points, 1.))
#print(myhours)

#generate days for trip
mydays = numpy.random.random_integers(0, 7)
#print(mydays)

#call function
cluster(mydata,myhours,mydays, 10)