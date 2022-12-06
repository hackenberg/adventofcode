def p1(f):
    data = f.read().split('\n')[:-1]
    return sum([fully_contains(r) for r in map(split_row, data)])


def split_row(row):
    return [s.split('-') for s in row.split(',')]


def fully_contains(row):
    sl = int(row[0][0]) # start of left range
    el = int(row[0][1]) # end of left range
    sr = int(row[1][0]) # start of right range
    er = int(row[1][1]) # end of right range
    return (sl <= sr and el >= er) or (sl >= sr and el <= er)


def p2(f):
    data = f.read().split('\n')[:-1]
    return sum([overlaps(r) for r in map(split_row, data)])


def overlaps(row):
    sl = int(row[0][0]) # start of left range
    el = int(row[0][1]) # end of left range
    sr = int(row[1][0]) # start of right range
    er = int(row[1][1]) # end of right range
    if sl <= sr:
        return el >= sr
    else:
        return er >= sl
