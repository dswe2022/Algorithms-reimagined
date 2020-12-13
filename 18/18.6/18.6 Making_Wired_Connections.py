
#EOPL 18.6
#Design an algorithm that takes a pins and a set of wires connecting pairs of pins,
#and determines if it is possible to place some pins on the left half of a PCB.
#Time: O(p+w) -> p is number of pins and w is number of wires.
#Space: O(p) -> p is number of pins.

class GraphVertex:
        def __init__(self):
            self.d = -1
            self.edges = []



def is_any_placement_fesible(G):
    def bfs(s):
        s.d = 0
        q = collections.deque([s])

        while q:
            for t in q[0].edges:
                if t.d == -1:
                    t.d = q[0].d + 1
                    q.qppend(t)
                elif t.d == q[0].d:
                    return False
            del q[0]

        return True

    return all(bfs(v) for v in G if v.d == -1)
