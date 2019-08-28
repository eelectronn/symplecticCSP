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

sh_and_m = [[[1 for _ in range(i)], i] for i in range(2, 11)]

sh_and_m = [
    [[2, 1], 2],
    [[3, 1], 2],
    [[4, 1], 2],
    [[5, 1], 2],
    [[2, 1, 1], 3],
    [[3, 1, 1], 3],
    [[4, 1, 1], 3],
    [[5, 1, 1], 3],
    [[2, 1, 1, 1], 4],
    [[3, 1, 1, 1], 4],
    [[4, 1, 1, 1], 4],
    [[5, 1, 1, 1], 4],
    [[2, 1, 1, 1, 1], 5],
    [[3, 1, 1, 1, 1], 5],
    [[4, 1, 1, 1, 1], 5],
    [[5, 1, 1, 1, 1], 5],
]

sh_and_m = [[[2, 1, 1, 1, 1], 5]]

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
