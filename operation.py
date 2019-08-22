import alphabet as a


def f_i(t, i, m):
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
