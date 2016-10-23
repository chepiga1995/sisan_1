__author__ = 'craig'

import scipy.sparse.linalg
from numpy import *
import Polinoms


class Compute:
    def __init__(self, data, polynom_type, pol_pow_x1, pol_pow_x2, pol_pow_x3, bq0AsAvg, lambda_separate):
        # making appropriate vector bq0
        bq0 = []
        if bq0AsAvg:
            for y in data.data_y:
                bq0.append((max(y) + min(y))/2.)
            bq0 = [bq0]
        else:
            bq0 = list(map(list, zip(*data.data_y)))

        # Generate matrix A
        A = []
        A_x1 = []
        A_x2 = []
        A_x3 = []

        if lambda_separate:
            print("Should be for separate")
            A_x1 = generate_A_separate(data.data_x1, pol_pow_x1, polynom_type)
            A_x2 = generate_A_separate(data.data_x2, pol_pow_x2, polynom_type)
            A_x3 = generate_A_separate(data.data_x3, pol_pow_x3, polynom_type)
        else:
            print("for all lambda")
            A = generate_A_all(data.data_x1, data.data_x2, data.data_x3, pol_pow_x1, pol_pow_x2, pol_pow_x3, polynom_type)

        # indeed minimization
        Lambda = []
        if lambda_separate:
            for b in bq0:
                Lambda1 = minimization(A_x1, [b], 10000)
                Lambda2 = minimization(A_x2, [b], 10000)
                Lambda3 = minimization(A_x3, [b], 10000)
                Lambda.append(Lambda1[0] + Lambda2[0] + Lambda3[0])
        else:
            Lambda = minimization(A, bq0, 10000)

        # Checking Lambda solving
        #print Lambda
        #print "ERROR for lambda="
        #print norma_delta(A, Lambda, bq0[0])

        # find PSI matrix
        PSI_x1 = []
        PSI_x2 = []
        PSI_x3 = []
        a = []
        c = []
        for i in range(0, array(data.data_y).shape[1]):
            if array(Lambda).shape[0] == 1:
                print(" only LAMBDA[0]")
                PSI_x1 = PSI_def(data.data_x1, pol_pow_x1, polynom_type, Lambda[0], 0)                         # 45*dim_x1
                PSI_x2 = PSI_def(data.data_x2, pol_pow_x2, polynom_type, Lambda[0], pol_pow_x1+1)              # 45*dim_x2
                PSI_x3 = PSI_def(data.data_x3, pol_pow_x3, polynom_type, Lambda[0], pol_pow_x1+1+pol_pow_x2+1) # 45*dim_x3
            elif array(Lambda).shape[0] > 1:
                PSI_x1 = PSI_def(data.data_x1, pol_pow_x1, polynom_type, Lambda[i], 0)                         # 45*dim_x1
                PSI_x2 = PSI_def(data.data_x2, pol_pow_x2, polynom_type, Lambda[i], pol_pow_x1+1)              # 45*dim_x2
                PSI_x3 = PSI_def(data.data_x3, pol_pow_x3, polynom_type, Lambda[i], pol_pow_x1+1+pol_pow_x2+1) # 45*dim_x3
            else:
                print("Error in Lambda dimensional")

            # find three parts a
            a1 = []
            a2 = []
            a3 = []

            #print array(PSI_x1).shape

            a1.append((minimization(PSI_x1, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])
            a2.append((minimization(PSI_x2, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])
            a3.append((minimization(PSI_x3, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])

            #print "a1="
            #print a1
            #print "a2="
            #print a2
            #print "a3="
            #print a3

            # checking a solving
            #print "ERROR a1="
            #print norma_delta(PSI_x1, a1[0], list(map(list, zip(*data.data_y)))[i])
            #print "ERROR a2="
            #print norma_delta(PSI_x2, a2[0], list(map(list, zip(*data.data_y)))[i])
            #print "ERROR a3="
            #print norma_delta(PSI_x3, a3[0], list(map(list, zip(*data.data_y)))[i])

            a.append(a1[0] + a2[0] + a3[0])
            # find a
            #PSI = union(union(PSI_x1, PSI_x2), PSI_x3)
            #a.append((minimization(PSI, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])
            #print PSI
            # checking a solving
            #print "ERROR a="
            #print norma_delta(PSI, a[i], list(map(list, zip(*data.data_y)))[i])

            # Generate PHI matrix
            PHI_TREE = def_PHI(data, PSI_x1, PSI_x2, PSI_x3, a[i])
            #print PHI_TREE
            c.append((minimization(PHI_TREE, [list(map(list, zip(*data.data_y)))[i]], 10000))[0])
            #print array(c).shape
            # checking c solving
            print("ERROR c=")
            print(c)
            print(norma_delta(PHI_TREE, c[i], list(map(list, zip(*data.data_y)))[i]))







def generate_A_separate(x1, pow_x1, pol_type):
    A = []
    pol_class = Polinoms.polinom()

    for x in x1:
        row_A = []
        for x_i in x:
            row_polinom = []
            for j in range(0, pow_x1+1):
                row_polinom.append(getattr(pol_class, pol_type)(j, x_i))
            row_A += row_polinom
        A.append(row_A)
    return A


def generate_A_all(x1, x2, x3, pow_x1, pow_x2, pow_x3, pol_type):
    A = []
    pol_class = Polinoms.polinom()

    temp = list(map(list, zip(x1, x2, x3)))
    for x_1, x_2, x_3 in temp:
        row_A =[]
        for x_i in x_1:
            row_polinom = []
            for j in range(0, pow_x1+1):
                row_polinom.append(getattr(pol_class, pol_type)(j, x_i))
            row_A += row_polinom
        for x_i in x_2:
            row_polinom = []
            for j in range(0, pow_x2+1):
                row_polinom.append(getattr(pol_class, pol_type)(j, x_i))
            row_A += row_polinom
        for x_i in x_3:
            row_polinom = []
            for j in range(0, pow_x3+1):
                row_polinom.append(getattr(pol_class, pol_type)(j, x_i))
            row_A += row_polinom
        A.append(row_A)

    return A


def minimization(A, bq0, iter, start=None):
    A_new = dot(array(A).transpose(), array(A))
    bq0_new = []
    for b in bq0:
        bq0_new.append(dot(array(A).transpose(), b))
    Lambda = []

    a_sparse = scipy.sparse.csc_matrix(A_new)
    y_index = 0

    for b in bq0_new:
        result, error = scipy.sparse.linalg.cg(a_sparse, b, None, 1e-8, iter)
        Lambda.append(list(result))
        #print "Minimization statistic:"
        #print "for y" + str(y_index) + " computational error=" + str(error)
        y_index += 1

    return Lambda

def PSI_def(x, pol_pow, poly_type, Lambda, lambda_index):
    PSI_x = []
    for x_vector in x:
        PSI_x_row = []
        for x_i in x_vector:
            pol_class = Polinoms.polinom()
            psi_temp = 0.
            for p in range(0, pol_pow+1):
                psi_temp += Lambda[lambda_index+p]*getattr(pol_class, poly_type)(p, x_i)
            PSI_x_row.append(psi_temp)
        PSI_x.append(PSI_x_row)
    return PSI_x


def norma_delta(A_, x_, b_):
    left = dot(array(A_), array(x_).transpose())
    right = b_
    temp = list(map(list, zip(left, right)))
    norma = 0
    for a1, a2 in temp:
        norma += (a1-a2)*(a1-a2)
    return sqrt(norma)

def union(temp1, temp2):
    temp1 = array(temp1).transpose()
    temp1 = list(temp1)
    temp2 = array(temp2).transpose()
    temp2 = list(temp2)
    for row in temp2:
        temp1.append(row)
    return list(array(temp1).transpose())


def def_PHI(data_, PSI_x1_, PSI_x2_, PSI_x3_, a_):
    PHI_ = []

    dim_x1 = array(data_.data_x1).shape[1]
    dim_x2 = array(data_.data_x2).shape[1]
    dim_x3 = array(data_.data_x3).shape[1]
    for i_1 in range(0, array(data_.data_y).shape[0]):
        row_PHI = []
        phi_func = 0
        for j_1 in range(0, dim_x1):
            phi_func += a_[j_1]*PSI_x1_[i_1][j_1]
        row_PHI.append(phi_func)
        phi_func = 0
        for j_1 in range(0, dim_x2):
            phi_func += a_[dim_x1+j_1]*PSI_x2_[i_1][j_1]
        row_PHI.append(phi_func)
        phi_func = 0
        for j_1 in range(0, dim_x3):
            phi_func += a_[dim_x1+dim_x2+j_1]*PSI_x3_[i_1][j_1]
        row_PHI.append(phi_func)
        PHI_.append(row_PHI)
    return PHI_