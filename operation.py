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
