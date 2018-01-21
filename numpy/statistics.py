import numpy as np

x = np.random.random((1000, 20))

y = np.arange(20).reshape(1, 20)

print(str(x[0]))
print(x[0])

x_min = np.amin(x[0])

print("x type:" + str(type(x[0][0])))
print(x[0][0])
print("x_min type:" + str(type(x_min)))
print(x_min)

print(min(x[0]))

print(min([ 0.74497599,0.69699397,0.78497642,0.89425431,0.73276478,0.79950467
,0.36359341,0.15052367,0.05043552,0.30086801,0.56971331,0.27345042
,0.36843153,0.39685848,0.86348986,0.50866996,0.39094865,0.106036
,0.36954412,0.67056489]))


print(np.amin(y[0]))