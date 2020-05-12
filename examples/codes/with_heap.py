def dijkstraHeap(G,s, t):
    hp = Heap()
    bw =  [0] * V
    parent =[-1] * V
    status = [2] * V

    status[s] = 0
    bw[s] = sys.maxsize
    for v in G.finderNeighbor(s):
        bw[v.dst] = v.bw
        parent[v.dst] = s
        status[v.dst] = 1
        hp.insert(v.dst, bw[v.dst])
    
    while status[t] != 0:
        v = hp.maximum()
        hp.delete(hp.maximum())
        status[v] = 0
        n = G.findNeighbor(v)
        for i in range(len(n)):
            w = n[i].dst
            if (status[w] == 2):
                bw[w] = min(bw[v], n[i].bw)
                parent[w] = v
                status[w] = 1
                hp.insert(w, bw[w])
            elif (status[w] == 1 and bw[w] < min(bw[v], n[i].bw)):
                hp.delete(w)
                bw[w] = min(bw[v], n[i].bw)
                parent[w] = v
                hp.insert(w.bw[w])
    return bw[t]