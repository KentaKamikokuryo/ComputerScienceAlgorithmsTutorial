from collections import deque


class Graph:

    def __init__(self, edges, n):

        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:

            # 頂点 src から 頂点 dest まで辺を張る
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


def BFS(graph, v, discovered):

    q = deque()

    discovered[v] = True

    # キューの後に追加
    q.append(v)

    while q:

        # キューの前から取り出して，vに格納
        v = q.popleft()
        print(v, end=" ")

        for u in graph.adjList[v]:
            if not discovered[u]:
                discovered[u] = True
                q.append(u)


if __name__ == '__main__':

    # 上の図によるグラフエッジ（辺）のリスト
    # (A_i, B_i) i本目の辺は，頂点A_iと頂点B_iを結ぶ．
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # 頂点0、13、および14は単一ノードです
    ]

    # グラフ内のノードの総数(0から14までのラベルが付いています)
    n = 15

    # は、指定されたエッジからグラフを作成します
    graph = Graph(edges, n)

    # ノードが検出されたかどうかを追跡する
    # 各ノードが何手目に探索されたか
    # False は「まだ探索されていない」を表す
    discovered = [False] * n

    # すべての未検出ノードからBFSトラバーサルを実行して
    # は、グラフのすべての連結成分をカバーします
    for i in range(n):
        if not discovered[i]:
            # は頂点iからBFSトラバーサルを開始します
            BFS(graph, i, discovered)


