import pygame

import node
import math


class search(object):

    def __init__(self, map, x, y):
        self.map = map
        self.x = x
        self.y = y

    def astarSearch(self, target_node):
        target = self.astar(target_node)
        path = []
        while target.parent != 0:
            target = target.parent
            target.draw_path()
        print(target.x)
        print(target.y)

    def astar(self, target_node):

        pygame.display.update()
        open_nodes = []
        closed_nodes = []

        open_nodes.append(self.map[self.x][self.y])

        while len(open_nodes) > 0:

            q = open_nodes[0]

            for n in open_nodes:
                if n.f < q.f:
                    q = n

            open_nodes.remove(q)
            self.x = q.x
            self.y = q.y

            child_list = self.getChildren(q)

            for n in child_list:
                if n.goal:
                    return n

                n.g += q.g #+ math.sqrt(abs(self.x - q.x) ** 2 + abs(self.y - q.y) ** 2)
                #n.g = math.sqrt(abs(self.x ) ** 2 + abs(self.y ) ** 2)
                n.h = math.sqrt(abs(self.x - target_node.x) ** 2 + abs(self.y - target_node.y) ** 2)
                #n.h = abs(self.x - target_node.x) + abs(self.y - target_node.y)
                #n.h = max(abs(self.x - target_node.x), abs(self.y - target_node.y))
                f = n.g + n.h

                if n.open:
                    if n.f > f:
                        n.f = f
                    continue
                if n.closed:
                    continue

                n.f = f
                n.open = True
                open_nodes.append(n)
                n.visited()

            closed_nodes.append(q)
            q.close()

    def getChildren(self, q):

        children = []

        if self.x > 0:
            n = self.map[self.x - 1][self.y]
            if n.valid():
                n.parent = q
                n.g = 1
                children.append(n)
        if self.x < len(self.map) - 1:
            n = self.map[self.x + 1][self.y]
            if n.valid():
                n.parent = q
                n.g = 1
                children.append(n)
        if self.y > 0:
            n = self.map[self.x][self.y - 1]
            if n.valid():
                n.parent = q
                n.g = 1
                children.append(n)
        if self.y < len(self.map[0]) - 1:
            n = self.map[self.x][self.y + 1]
            if n.valid():
                n.parent = q
                n.g = 1
                children.append(n)
        # if self.x > 0 and self.y > 0:
        #     n = self.map[self.x - 1][self.y - 1]
        #     if n.valid():
        #         n.parent = q
        #         n.g = 1.4
        #         children.append(n)
        # if self.x > 0 and self.y < len(self.map) - 1:
        #     n = self.map[self.x - 1][self.y + 1]
        #     if n.valid():
        #         n.parent = q
        #         n.g = 1.4
        #         children.append(n)
        # if self.x < len(self.map[0]) - 1 and self.y > 0:
        #     n = self.map[self.x + 1][self.y - 1]
        #     if n.valid():
        #         n.parent = q
        #         n.g = 1.4
        #         children.append(n)
        # if self.x < len(self.map[0]) - 1 and self.y < len(self.map) - 1:
        #     n = self.map[self.x + 1][self.y + 1]
        #     if n.valid():
        #         n.parent = q
        #         n.g = 1.4
        #         children.append(n)
        return children
