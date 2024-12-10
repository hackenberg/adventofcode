from utils import *

#import IPython; IPython.embed(colors="neutral")
#import ipdb; ipdb.set_trace()

def p1(text: str) -> any:
    in1 = parse(text, digits)[0]  # input is single line
    blocks = list(to_blocks(in1))
    #print(blocks)

    i, j = -1, len(blocks) - 1
    while i < j:
        i += 1

        #print("".join(blocks))

        if blocks[i] != ".":
            continue
 
        if blocks[j] == ".":
            i -= 1
            j -= 1
            continue

        blocks[i] = blocks[j]
        blocks[j] = "."
        j -= 1

    #print("".join(blocks))
    return checksum(blocks)
    #return len(in1)


def print_blocks(seq):
    for fileid, (filelen, spacelen) in enumerate(zip(seq[::2], seq[1::2] + (0,))):
        #print(i, filelen, spacelen)
        #fileid = str(i // 2)
        #filelen, spacelen = c
        print(str(fileid) * filelen, '.' * spacelen)


def to_blocks(seq):
    def fn(args):
        block = ['.'] if args[0] % 2 != 0 else [str(args[0] // 2)]
        return block * args[1]
    return flatten(map(fn, enumerate(seq)))


def checksum(blocks):
    return sum(i * int(d) for i, d in enumerate(blocks) if d != ".")


def p2(text: str) -> any:
    in2 = parse(text)
