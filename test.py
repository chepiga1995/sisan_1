__author__ = 'craig'

from numpy import *
import scipy.sparse.linalg

a = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

b = [2, 2, 2]

a = array(a)
A = scipy.sparse.csc_matrix(a)
x, er = scipy.sparse.linalg.cg(A, b)

print A

print x
print er

a = [[1, 2, 3],
     [4, 5, 6]]
b = [9, 9, 9]

c = list(map(list, zip(a, b)))
for x, y in c:
    print x
    print y

x1 = [[1, 1, 1],
      [1, 1, 1]]
x2 = [[2, 2],
      [2, 2]]

print x1 + x2

o = array([[-1, 1],
     [1, -1]]).transpose()
r = array([[2],
           [1]])
s = dot(o, r)
print type(s)
print o.transpose()

l1 = [[1, 2, 3], [1, 2, 3]]

print "l1="
print l1[1][2]
print array(l1).shape[0]


a1 = array([[1, 2, 3],
      [1, 2, 3]])

a2 = array([[1],
      [1]])

def union(temp1, temp2):
    temp1 = a1.transpose()
    temp1 = list(temp1)
    temp2 = a2.transpose()
    temp2 = list(temp2)
    for row in temp2:
        temp1.append(row)
    return list(array(temp1).transpose())


'''
        PSI_x1 = []
        PSI_x2 = []
        PSI_x3 = []
        for i in range(0, array(data.data_y).shape[1]):
            if array(Lambda).shape[0] == 1:
                print " only LAMBDA[0]"
                PSI_x1 = PSI_def(data.data_x1, pol_pow_x1, polynom_type, Lambda[0], 0) # 45*dim_x1
                PSI_x2 = PSI_def(data.data_x2, pol_pow_x2, polynom_type, Lambda[0], pol_pow_x1+1) # 45*dim_x2
                PSI_x3 = PSI_def(data.data_x3, pol_pow_x3, polynom_type, Lambda[0], pol_pow_x1+1+pol_pow_x2+1) # 45*dim_x3
            elif array(Lambda).shape[0] > 1:
                PSI_x1 = PSI_def(data.data_x1, pol_pow_x1, polynom_type, Lambda[i], 0) # 45*dim_x1
                PSI_x2 = PSI_def(data.data_x2, pol_pow_x2, polynom_type, Lambda[i], pol_pow_x1+1) # 45*dim_x2
                PSI_x3 = PSI_def(data.data_x3, pol_pow_x3, polynom_type, Lambda[i], pol_pow_x1+1+pol_pow_x2+1) # 45*dim_x3
            else:
                print "Error in Lambda dimensional"

            # find three parts a
            a1 = []
            a2 = []
            a3 = []

            print array(PSI_x1).shape
            x0 = list(map(list, zip(*data.data_y)))[i]
            for r in x0:
                r=1
            start = []
            for j in range(0, 25):
                start.append(1)

            a1.append((minimization(PSI_x1, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])
            a2.append((minimization(PSI_x2, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])
            a3.append((minimization(PSI_x3, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])

            print "a1="
            print a1
            print "a2="
            print a2
            print "a3="
            print a3

            # checking a solving
            print "ERROR a1="
            print norma_delta(PSI_x1, a1[0], list(map(list, zip(*data.data_y)))[i])
            print "ERROR a2="
            print norma_delta(PSI_x2, a2[0], list(map(list, zip(*data.data_y)))[i])
            print "ERROR a3="
            print norma_delta(PSI_x3, a3[0], list(map(list, zip(*data.data_y)))[i])'''