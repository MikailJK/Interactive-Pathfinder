import pygame
import node

window_width = 1000
window_height = 1000
nodes = []

def main():
    pygame.init()
    win = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Interactive Pathfinder")

    win.fill((255, 255, 255))

    #creates nodes 
    for i in range(50):
        for j in range(50):
            n = node.node(20 * i, 20 * j, 20, 20, i + j)
            nodes.append(n)
            n.draw(win)

    drag = False

    run = True
    while run:

        for e in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if e.type == pygame.QUIT:
                run = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(nodes)):
                    if nodes[i].isOver(pos):
                        nodes[i].clicked(win)
                drag = True

            if e.type == pygame.MOUSEBUTTONUP:
                drag = False

            if e.type == pygame.MOUSEMOTION and drag:
                for i in range(len(nodes)):
                    if nodes[i].isOver(pos):
                        nodes[i].clicked(win)
                drag = True


        for i in range(len(nodes)):
            nodes[i].draw(win)

        pygame.display.update()






if __name__ == '__main__':
    main()
