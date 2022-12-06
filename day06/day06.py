def p1(f):
    data = f.read()
    for i in range(3, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i


def p2(f):
    data = f.read()
    for i in range(13, len(data)):
        if len(set(data[i-14:i])) == 14:
            return i
