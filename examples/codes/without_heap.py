def dijkstra(G, s, t):
    bw = [0] * V
    parent = [-1] * V
    status = [2] * V

    status[s] = 0
    bw[s] = sys.maxsize
    for v in G.findNeighbor(s):
        bw[b.dst] = v.bw
        parent[v.dst] = s
        status[v.dst] = 1

    while status[t] != 0:
        v=maxfringe(bw, status)
        status[v] = 0
        n= G.findNeighbor(v)
        for i in range(len(n)):
            w=n[i].dst
            if(status[w == 2]):
                bw[w] = min(bw[v], n[i].bw)
                parent[w] = V
                status[w] = 1
            elif (status[w] == 1 and bw[w] < min (bw[v], n[i].bw)):
                bw[w] = min(bw[v], n[i].bw)
                parent[w] = V
    return bw[t]