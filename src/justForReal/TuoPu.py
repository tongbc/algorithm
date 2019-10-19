def topsort(G):
    in_degrees = dict((u, 0) for u in G)
    for u in G:
        for v in  G[u]:
            in_degrees[v] += 1
                                    # 每一个节点的入度
    Q = [u for u in G if in_degrees[u] == 0]
                                    # 入度为 0 的节点
    S = []
    while Q:
        u = Q.pop()
                                    # 默认从最后一个移除
        S.append(u)
        for v in G[u]:
            in_degrees[v] -= 1
                                    # 并移除其指向
            if in_degrees[v] == 0:
                Q.append(v)
    return S

G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
# ['a', 'b', 'c', 'd', 'e', 'f']

def tp(G):
    indgrees = dict((u,0) for u in G)
    for u in G:
        for v in G[u]:
            indgrees[v]+=1
    zero = [n for n in indgrees if indgrees[n]==0]
    res = []
    while(zero):
        p = zero.pop()
        res.append(p)
        for v in G[p]:
            indgrees[v]-=1
            if  indgrees[v]==0:
                zero.append(v)
    return res

print(tp(G))
