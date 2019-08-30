"""
This module contains all the elementary function to apply action c on a kn tableau.
"""
import alphabet as a
import tableau as tab
import sympy as sp


def f_i(t, i, m, mutable=True):
    """
    Function to apply f_i on tableau.

    :param t: tableau.
    :param i: i as in f_i
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :param mutable: optional. Default set to True, where it directly make changes to the tableau t. If passed in as False, it creates a copy of t and operates on that copy, leaving t unaffected.
    :return: tableau after applying f_i
    """
    if not mutable:
        t = t.clone()
    o_lower, o_higher = a.Ordinary(i), a.Ordinary(i + 1)
    b_lower, b_higher = a.Barred(i + 1), a.Barred(i)
    pos, stack = None, 0
    for y in range(len(t.shapeTranspose)):
        col_len = t.shapeTranspose[y]
        for x in range(col_len):
            if t.body[col_len-x-1][y] == o_lower or t.body[col_len-x-1][y] == b_lower:
                if stack == 0:
                    pos = [col_len-x-1, y]
                else:
                    stack -= 1
            elif t.body[col_len-x-1][y] == o_higher or t.body[col_len-x-1][y] == b_higher:
                stack += 1
    if pos is None:
        return None
    if i == m:
        num = t.body[pos[0]][pos[1]].num
        t.body[pos[0]][pos[1]] = a.Barred(num)
        return t
    if isinstance(t.body[pos[0]][pos[1]], a.Ordinary):
        t.body[pos[0]][pos[1]].num += 1
    else:
        t.body[pos[0]][pos[1]].num -= 1
    return t


def e_i(t, i, m, mutable=True):
    """
    Function to apply e_i on tableau.

    :param t: tableau.
    :param i: i as in e_i
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :param mutable: optional. Default set to True, where it directly make changes to the tableau t. If passed in as False, it creates a copy of t and operates on that copy, leaving t unaffected.
    :return: tableau after applying e_i
    """
    if not mutable:
        t = t.clone()
    o_lower, o_higher = a.Ordinary(i), a.Ordinary(i+1)
    b_lower, b_higher = a.Barred(i+1), a.Barred(i)
    pos, stack = None, 0
    for y in range(len(t.shapeTranspose)):
        for x in range(t.shapeTranspose[-y-1]):
            if t.body[x][len(t.shapeTranspose)-y-1] == o_higher or t.body[x][len(t.shapeTranspose)-y-1] == b_higher:
                if stack == 0:
                    pos = [x, len(t.shapeTranspose)-y-1]
                else:
                    stack -= 1
            elif t.body[x][len(t.shapeTranspose)-y-1] == o_lower or t.body[x][len(t.shapeTranspose)-y-1] == b_lower:
                stack += 1
    if pos is None:
        return None
    if i == m:
        num = t.body[pos[0]][pos[1]].num
        t.body[pos[0]][pos[1]] = a.Ordinary(num)
        return t
    if isinstance(t.body[pos[0]][pos[1]], a.Ordinary):
        t.body[pos[0]][pos[1]].num -= 1
    else:
        t.body[pos[0]][pos[1]].num += 1
    return t


def get_crystal_graph(shape, m=None):
    """
    Function to create crystal graph data.

    :param shape: shape of tableaux in graph
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :return: a list of all k-n tableaux for given shape and value of m, an f_i dictionary with all the kn tableaux as keys with a list as value, where (i-1)st index in list refer to tableau obtained by applying f_i to the key tableau. A similar e_i tableaux dictionary.
    """
    if m is None:
        m = len(shape)
    starting_tableau = tab.Tableau([[a.Ordinary(i+1) for _ in range(shape[i])] for i in range(len(shape))])
    tableaux = [starting_tableau]
    fi_map, ei_map = dict(), dict()
    ei_map[starting_tableau] = [None for _ in range(m)]
    index = 0
    while index < len(tableaux):
        t = tableaux[index]
        fi_map[t] = f = [None for _ in range(m)]
        for i in range(m):
            f_of_t = f_i(t, i+1, m, False)
            if f_of_t is not None:
                if f_of_t in ei_map:
                    e = ei_map[f_of_t]
                else:
                    e = [None for _ in range(m)]
                    ei_map[f_of_t] = e
                    tableaux.append(f_of_t)
                f[i] = f_of_t
                e[i] = t
        index += 1
    return tableaux, fi_map, ei_map


def get_tableaux_set(shape, m=None):
    """
    Function to obtain all the kn tableaux of given shape and value of m.

    :param shape: shape of tableaux.
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :return: list of all the tableaux of given shape and value of m.
    """
    tableaux, fi_map, ei_map = get_crystal_graph(shape, m)
    return tableaux


def s_i(t, i, m=None, mutable=True):
    """
    Function to apply s_i to the tableau.

    :param t: tableau.
    :param i: i as in s_i
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :param mutable: optional. Default set to True, where it directly make changes to the tableau t. If passed in as False, it creates a copy of t and operates on that copy, leaving t unaffected.
    :return: tableau obtained after applying s_i on t.
    """
    if not mutable:
        t = t.clone()
    i_count = i_plus_one_count = 0
    o_i, o_i_plus_one = a.Ordinary(i), a.Ordinary(i+1)
    b_i, b_i_plus_one = a.Barred(i), a.Barred(i+1)
    for x in range(len(t.body)):
        for y in range(len(t.body[x])):
            if t.body[x][y] == o_i:
                i_count += 1
            elif t.body[x][y] == o_i_plus_one:
                i_plus_one_count += 1
            elif t.body[x][y] == b_i:
                i_count -= 1
            elif t.body[x][y] == b_i_plus_one:
                i_plus_one_count -= 1
    k = i_count - i_plus_one_count
    if k >= 0:
        task = f_i
    else:
        task = e_i
        k = -k
    for _ in range(k):
        task(t, i, m)
    return t


def action_c(t, m=None, mutable=True):
    """
    Function to apply action c on tableau.

    :param t: tableau.
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :param mutable: optional. Default set to True, where it directly make changes to the tableau t. If passed in as False, it creates a copy of t and operates on that copy, leaving t unaffected.
    :return: tableau obtained after applying c on t.
    """
    if not mutable:
        t = t.clone()
    for i in range(m):
        s_i(t, m-i, m)
    return t


def order_of_tableau(t, m=None):
    """
    Function to compute the order of action c.

    :param t: tableau.
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :return: order of tableau t under action c.
    """
    t_copy = t.clone()
    action_c(t_copy, m)
    order = 1
    while t != t_copy:
        action_c(t_copy, m)
        order += 1
    return order


def order_of_set(shape, m=None):
    """
    Function to compute order of a set of kn tableaux of a given shape and value of m.

    :param shape: shape of tableau.
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :return: dictionary with key as order and frequency of that order in set as value of that key.
    """
    tableaux = get_tableaux_set(shape, m)
    order_freq = {}
    for t in tableaux:
        order = order_of_tableau(t, m)
        if order in order_freq:
            order_freq[order] += 1
        else:
            order_freq[order] = 1
    return order_freq


def get_power_of_q(t, m):
    """
    Power of q in the monomial that corresponds to tableau.

    :param t: tableau.
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :return: power of q in the monomial that corresponds to tableau t.
    """
    monomial = [0 for _ in range(m)]
    for i in range(len(t.body)):
        for j in range(len(t.body[i])):
            if isinstance(t.body[i][j], a.Ordinary):
                monomial[t.body[i][j].num - 1] += 1
            else:
                monomial[t.body[i][j].num - 1] -= 1
    power_of_q = 0
    for i in range(m):
        power_of_q += i*monomial[i]
    return power_of_q


def get_kn_schur_polynomial(shape, m=None):
    """
    Function to compute the kn-Schur polynomial in q for a given shape and value of m.

    :param shape: shape of tableaux in set.
    :param m: m such that allowed entries in t are 1 to m and 1-bar to m-bar
    :return: Schur polynomial in variable q. and variable q.
    """
    tableaux = get_tableaux_set(shape, m)
    polynomial = 0
    q = sp.symbols('q')
    for t in tableaux:
        monomial = get_power_of_q(t, m)
        polynomial = polynomial + q**monomial
    return polynomial, q


def nth_root_of_unity(n):
    """
    Function to compute n-th root of unity.

    :param n: n as in n-th root of unity.
    :return: n-th root of unity in form of sympy complex number expression.
    """
    return sp.exp(2*sp.pi*sp.I/n).expand(complex=True)


def k_of_shape(shape):
    """
    statistic of shape as defined in OH's and PARK's paper.

    :param shape: shape.
    :return: statistic of shape.
    """
    k = 0
    for i in range(len(shape)):
        k += i*shape[i]
    return k


def evaluate(poly, q, inp):
    """
    Function to evaluate polynomial at a particular value.

    :param poly: polynomial.
    :param q: variable in polynomial.
    :param inp: input value where we need to evaluate the polynomial.
    :return: value obtained after evaluation.
    """
    return poly.subs(q, inp).expand(complex=True)
