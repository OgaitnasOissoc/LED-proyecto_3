import os
import sys
import logic
import time
import networkx as nx
import matplotlib.pyplot as plt

def make_folder():
    name = f"pandemic{time.time()}"
    direc = os.path.join(os.getcwd(), name)
    os.makedirs(direc)
    return direc


def make_image(dire, pan, p):
    color_map = []
    for i in pan.map.nodes:
        if pan.map.nodes[i]["status"] == "infected":
            color_map.append("red")
        else:
            color_map.append("white")
    nx.draw(pan.map, node_color=color_map, with_labels=True)
    plt.savefig(os.path.join(dire,f"day{p}.png"))
    plt.clf()
    plt.close()


def check_allinfected(pan):
    for j in pan.map.nodes:
        if pan.map.nodes[j]["status"] == "healthy":
            return
    sys.exit(0)


a = sys.argv[1]
s = sys.argv[2]
l = int(sys.argv[3])
pan = logic.Pandemic(a,s)

loc = make_folder()
make_image(loc, pan, 0)
for i in range(l):
    check_allinfected(pan)
    pan.progress()
    make_image(loc,pan,i+1)
