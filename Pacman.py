class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.parent = None
        self.g = 0
        self.h = 0

def frontier(point, grid):
    x = point.x
    y = point.y
    neighbours = []
    out = []
    for neighbour in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
        neighbours.append(grid[neighbour[0]][neighbour[1]])
    for neighbour in neighbours:
        if neighbour.value != '%':
            out.append(neighbour)
    return out



def manhattanDistance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)


def AStar(start, goal, grid):

    openset = {start}
    closedset = set()
    while openset:
        currentNode = min(openset, key=lambda o: o.g + o.h)
        if currentNode == goal:
            path = []
            while currentNode.parent:
                path.append(currentNode)
                currentNode = currentNode.parent
            path.append(currentNode)
            return path[::-1]

        openset.remove(currentNode)
        closedset.add(currentNode)

        for node in frontier(currentNode, grid):
            if node in closedset:
                continue
            if node in openset:
                if currentNode.value == '.':
                    new_g = currentNode.g
                else:
                    new_g = currentNode.g + 1
                if node.g > new_g:
                    node.g = new_g
                    node.parent = currentNode
            else:
                if currentNode.value == '.':
                    node.g = currentNode.g
                else:
                    node.g = currentNode.g + 1
                node.h = manhattanDistance(node, goal)
                node.parent = currentNode
                openset.add(node)

if __name__ == '__main__':

    pacman_xy = input().split()
    pacman_x = int(pacman_xy[0])
    pacman_y = int(pacman_xy[1])

    food_xy = input().split()
    food_x = int(food_xy[0])
    food_y = int(food_xy[1])

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    grid = []
    for i in range(n):
        grid.append(list(input().strip()))

    for x in range(n):
        for y in range(m):
            grid[x][y] = Node(x, y, grid[x][y])

    path = AStar(grid[pacman_x][pacman_y], grid[food_x][food_y], grid)

    for node in path:
        print(node.x, node.y)



# 3 9
# 5 1
# 7 20
# %%%%%%%%%%%%%%%%%%%%
# %--------------%---%
# %-%%-%%-%%-%%-%%-%-%
# %--------P-------%-%
# %%%%%%%%%%%%%%%%%%-%
# %.-----------------%
# %%%%%%%%%%%%%%%%%%%%