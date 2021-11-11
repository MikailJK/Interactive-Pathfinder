import pygame
import node
import button
from math import floor
import search

window_width = 1000
window_height = 1000
node_size = 20
tool_bar_height = 100
number_of_nodes_x = floor((window_width) / node_size)
number_of_nodes_y = floor((window_height - tool_bar_height) / node_size)
nodes = [[0 for x in range(number_of_nodes_y)] for y in range(number_of_nodes_x)]
buttons = []


global selector
global special_nodes
global drag
drag = False
dummy_node = 0
start_node = 0
target_node = 0
special_nodes = [dummy_node, start_node, target_node]
selector = 0


def main():
    global selector
    global special_nodes
    global drag

    pygame.init()
    win = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Interactive Pathfinder")

    win.fill((142, 149, 163))

    buttons.append(button.button(500, 15, 70, 200, pygame.image.load("reset.png"), win, resetNodes))
    buttons.append(button.button(100, 15, 70, 200, pygame.image.load("start.png"), win, startSearch))
    buttons.append(button.button(800, 0, 33, 87, pygame.image.load("wall.png"), win, setSelectorWall))
    buttons.append(button.button(800, 33, 33, 87, pygame.image.load("start.png"), win, setSelectorStart))
    buttons.append(button.button(800, 66, 33, 87, pygame.image.load("end.png"), win, setSelectorEnd))

    # creates nodes
    resetNodes(win)



    run = True
    while run:

        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if e.type == pygame.QUIT:
                run = False

            if e.type == pygame.MOUSEBUTTONDOWN:

                if selector == 0:
                    drag = True

                for i in range(number_of_nodes_x):
                    for j in range(number_of_nodes_y):
                        if nodes[i][j].isOver(pos):

                            if selector != 0 and special_nodes[selector] != 0:
                                nodes[special_nodes[selector].x][special_nodes[selector].y].reset()
                                special_nodes[selector].reset()

                            special_nodes[selector] = nodes[i][j].clicked(win, selector)



                for i in range(len(buttons)):
                    if buttons[i].isOver(pos):
                        buttons[i].clicked(win)

            if (e.type == pygame.MOUSEMOTION and drag):
                for i in range(number_of_nodes_x):
                    for j in range(number_of_nodes_y):
                        if nodes[i][j].isOver(pos):
                            nodes[i][j].clicked(win, selector)

            if e.type == pygame.MOUSEBUTTONUP:
                drag = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and target_node != 0:
                    s = search.search(nodes, 0, 0)
                    s.astarSearch(target_node)

        for i in range(number_of_nodes_x):
            for j in range(number_of_nodes_y):
                nodes[i][j].draw()

        pygame.display.update()

def setSelectorWall(win):
    global selector
    global drag
    drag = True
    selector = 0


def setSelectorStart(win):
    global selector
    global drag
    drag = False
    selector = 1

def setSelectorEnd(win):
    global selector
    global drag
    drag = False
    selector = 2

def startSearch(win):
    global special_nodes

    if special_nodes[1] != 0 and special_nodes[2] != 0:
        s = search.search(nodes, special_nodes[1].x, special_nodes[1].y)
        s.astarSearch(special_nodes[2])


def resetNodes(win):

    global special_nodes
    if special_nodes[1] != 0:
        special_nodes[1].reset()
        special_nodes[1] = 0
    if special_nodes[2] != 0:
        special_nodes[2].reset()
        special_nodes[2] = 0

    for i in range(number_of_nodes_x):
        for j in range(number_of_nodes_y):
            n = node.node(node_size * i, (node_size * j) + tool_bar_height, node_size, i, j, win)
            nodes[i][j] = n
            n.draw()


if __name__ == '__main__':
    main()
