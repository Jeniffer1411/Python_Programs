lst = [12, 8, 90, 45, 3, 78, 34, 56]
def sortings(l):
    ol, el, res = [], [], []
    l.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            el.append(l[i])
        else:
            ol.append(l[i])
    for i in range(len(el)):
        for j in range(i + 1, len(el)):
            if el[i] < el[j]:
                el[i], el[j] = el[j], el[i]
    print(el)
    print(ol)
    e_count = 0
    o_count = 0
    for i in range(len(l)):
        if i % 2 == 0:
            res.append(el[e_count])
            e_count += 1
        else:
            res.append(ol[o_count])
            o_count += 1
    print(res)
sortings(lst)
