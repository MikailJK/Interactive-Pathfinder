import pygame
import node
from math import floor
import search

window_width = 1000
window_height = 1000
node_size = 20
number_of_nodes_x = floor(window_width / node_size)
number_of_nodes_y = floor(window_height / node_size)
nodes = [[0 for x in range(number_of_nodes_x)] for y in range(number_of_nodes_y)]

def main():
    pygame.init()
    win = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Interactive Pathfinder")

    win.fill((251, 251, 255))

    #creates nodes
    for i in range(number_of_nodes_x):
        for j in range(number_of_nodes_y):
            n = node.node(node_size * i, node_size * j, node_size, i, j, win)
            nodes[i][j] = n
            n.draw()


    target_node = 0

    drag = False

    run = True
    while run:

        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if e.type == pygame.QUIT:
                run = False

            if e.type == pygame.MOUSEBUTTONDOWN or (e.type == pygame.MOUSEMOTION and drag):
                for i in range(number_of_nodes_x):
                    for j in range(number_of_nodes_y):
                        if nodes[i][j].isOver(pos):
                            target_node = nodes[i][j].clicked(win, pygame.mouse.get_pressed())
                drag = True

            if e.type == pygame.MOUSEBUTTONUP:
                drag = False

            if e.type == pygame.KEYDOWN:
                s = search.search(nodes, 20, 20)
                s.astarSearch(target_node)




        for i in range(number_of_nodes_x):
            for j in range(number_of_nodes_y):
                nodes[i][j].draw()

        pygame.display.update()






if __name__ == '__main__':
    main()
