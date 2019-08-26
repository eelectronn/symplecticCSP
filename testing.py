import operation as o
import math

shape = [2, 2]
m = 2
# tableaux = o.get_tableaux_set(shape, m)
# for t in tableaux:
#     print(t)
# set_order = o.order_of_set(shape, m)
# print(set_order)
#
# polynomial = o.get_kn_schur_polynomial(shape, m)
# print(polynomial)
#
#
# def evaluate(poly, root):
#     i = root
#     sum = 0 + 0j
#     for k in poly:
#         sum += poly[k] * (pow(i, k))
#     print(sum)
#
#
# def nth_root_of_unity(n):
#     real = math.cos(2*2*math.pi/n)
#     img = math.sin(2*2*math.pi/n)
#     return complex(real, img)
#
#
# print(evaluate(polynomial, nth_root_of_unity(2*m)))
# print(len(o.get_tableaux_set([3, 3], 3)))
# # print(nth_root_of_unity(6))

tableaux = o.get_tableaux_set(shape, m)
for t in tableaux:
    print(t)
