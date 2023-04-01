class Graph:

    def __init__(self, edges, n):

        self.adjList = [[] for _ in range(n)]

        # は無向グラフにエッジを追加します
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# グラフ上のグラフでDFSトラバーサルを実行する#関数
def DFS(graph, v, discovered):
    discovered[v] = True  # は、現在のノードを検出済みとしてマークします
    print(v, end=' ')  # は現在のノードを出力します

    # はすべてのエッジに対して実行します(v、u)
    for u in graph.adjList[v]:
        if not discovered[u]:  # `u`がまだ発見されていない場合は
            DFS(graph, u, discovered)


if __name__ == '__main__':

    # 上の図によるグラフエッジのリスト
    edges = [
        # ノード0が接続されていないことに注意してください
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]

    # グラフ内のノードの総数(0から12までのラベルが付いています)
    n = 13

    # は、指定されたエッジからグラフを作成します
    graph = Graph(edges, n)

    # 頂点が検出されたかどうかを追跡する
    discovered = [False] * n

    # すべての未検出ノードからDFSトラバーサルを実行して
    # グラフのすべての連結成分をカバーします
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)
