import os
import networkx as nx
import matplotlib.pyplot as plt
from random import random

class Pandemic:
    def infect(self.n):
        self.map.nodes[n]["status"] = "infected"


    def __init__(self,location,starting):
        self.map = nx.from_edgelist(location)
        nx.set_node_attributes(self.map, {node: "healthy" for node in self.map.nodes}, "status")
        self.infect(starting)

    
    def progress(self):
        new_infected = []
        for node in self.map.nodes:
            if self.map.nodes[node]["status"] == "infected":
                for i in self.map.neighbors(node):
                    if self.map.nodes[i]["status"] == "healthy":
                        if random() >= 0.5:
                            new_infected.append(i)
        for g in new_infected:
            self.infect(g)

