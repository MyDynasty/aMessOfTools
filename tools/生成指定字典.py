data = []
ele = list('qwertyuiopasdfghjklzxcvbnm1234567890_-@')
a = list()


def creadict(n,ele):
    global a
    a, c = ele, ele
    for x in range(n):
        yield iter(a)
        c = (i+j for i in ele for j in a)
        a = list(c)

def main(n=5):
    tmp = creadict(n, ele)
    x2 = []
    for i in tmp:
        x2 = i
    print(type(x2))
    print(x2)

main(n=2)