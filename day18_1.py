class graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(cityAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(cityAry[row], end=' ')
        for col in range(g.SIZE):
            print("%2d" % g.graph[row][col], end=' ')
        print()
    print()


def find_vertex(g, vertx):
    stack = []
    visited_ary = []

    current = 0
    stack.append(current)
    visited_ary.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visited_ary:
                    pass
                else:
                    next = vertex
                    break

        if next is not None:
            current = next
            stack.append(current)
            visited_ary.append(current)
        else:
            current = stack.pop()

    if vertx in visited_ary:
        return True
    else:
        return False


cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
seoul, newyork, london, beijing, bangkok, paris = 0, 1, 2, 3, 4, 5


gSize = 6
G1 = graph(gSize)
G1.graph[seoul][newyork] = 80; G1.graph[seoul][beijing] = 10
G1.graph[newyork][seoul] = 80; G1.graph[newyork][beijing] = 40; G1.graph[newyork][bangkok] = 70
G1.graph[london][bangkok] = 30; G1.graph[london][paris] = 60
G1.graph[beijing][seoul] = 10; G1.graph[beijing][newyork] = 40; G1.graph[beijing][bangkok] = 50
G1.graph[bangkok][newyork] = 70; G1.graph[bangkok][beijing] = 50; G1.graph[bangkok][london] = 30; G1.graph[bangkok][paris] = 20
G1.graph[paris][bangkok] = 20; G1.graph[paris][london] = 60;

print('## all of graph ##')
print_graph(G1)

# 가중치 간선 목록
edgeAry = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edgeAry.append([G1.graph[i][k], i, k])

from operator import itemgetter

edgeAry = sorted(edgeAry, key=itemgetter(0), reverse=False)

newAry = []
for i in range(0, len(edgeAry), 2):
    newAry.append(edgeAry[i])

index = 0
while gSize - 1 < len(newAry):  # 간선의 개수가 '정점 개수-1'일 때까지 반복
    start = newAry[index][1]
    end = newAry[index][2]
    saveCost = newAry[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = find_vertex(G1, start)
    endYN = find_vertex(G1, end)

    if startYN and endYN:
        del (newAry[index])
    else:
        G1.graph[start][end] = saveCost
        G1.graph[end][start] = saveCost
        index += 1

print('## effective graph ##')
print_graph(G1)
