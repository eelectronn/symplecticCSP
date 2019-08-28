import operation as o

sh_and_m = [
    [[2, 1], 2],
    [[2, 1], 3],
    [[2, 2], 2],
    [[2, 2], 3],
    [[3, 2], 2],
    [[3, 2], 3],
    [[3, 3], 2],
    [[3, 3], 3],
    [[3, 2, 1], 3],
    [[3, 2, 2], 3],
    [[3, 3, 1], 3],
    [[3, 3, 2], 3],
    [[3, 3, 3], 3],
]

for sm in sh_and_m:
    print('shape: ' + str(sm[0]))
    print('m: ' + str(sm[1]))
    print('k(shape) = ' + str(o.k_of_shape(sm[0])))
    polynomial, q = o.get_kn_schur_polynomial(sm[0], sm[1])
    print('order and frequency =  ' + str(o.order_of_set(sm[0], sm[1])))
    print('p(q) = ' + str(polynomial))
    evaluation = o.evaluate(polynomial, q, o.nth_root_of_unity(2*sm[1]))
    print('p(2m^th root) = ' + str(evaluation))
    print()

