import alphabet as a
import tableau as tab


def f_i(t, i, m, mutable=True):
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
    tableaux, fi_map, ei_map = get_crystal_graph(shape, m)
    return tableaux


def s_i(t, i, m=None, mutable=True):
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
    if not mutable:
        t = t.clone()
    for i in range(m):
        s_i(t, m-i, m)
    return t


def order_of_tableau(t, m=None):
    t_copy = t.clone()
    action_c(t_copy, m)
    order = 1
    while t != t_copy:
        action_c(t_copy, m)
        order += 1
    return order


def order_of_set(shape, m=None):
    tableaux = get_tableaux_set(shape, m)
    order_freq = {}
    for t in tableaux:
        order = order_of_tableau(t, m)
        if order == 1:
            print(t)
        if order in order_freq:
            order_freq[order] += 1
        else:
            order_freq[order] = 1
    return order_freq


def get_monomial(t, m):
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
    tableaux = get_tableaux_set(shape, m)
    polynomial = {}
    for t in tableaux:
        monomial = get_monomial(t, m)
        if monomial in polynomial:
            polynomial[monomial] += 1
        else:
            polynomial[monomial] = 1
    return polynomial
